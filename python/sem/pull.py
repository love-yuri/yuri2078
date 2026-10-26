#!/usr/bin/env python3
"""
批量拉取 Git 仓库并执行 dotnet build
用法: python build_repos.py [--config config.json]
"""

import subprocess
import sys
import os
import json
import argparse
import shutil
from datetime import datetime
from pathlib import Path


# ─────────────────────────────────────────────
# 配置区：直接在这里添加/删除仓库
# 也可以通过 --config 指定外部 JSON 配置文件
# ─────────────────────────────────────────────
DEFAULT_REPOS = [
    {
        "url": "ssh://yidontekSW@192.168.101.93/volume1/GitRepo/SEMPro/SEM_DebugTools/ColumnClientWPF.git",
        "branch": "",  # 留空 "" 则使用默认分支
        "local_name": "",  # 克隆到本地的目录名；留空则自动从 URL 提取
        "build_args": [],  # 额外传给 dotnet build 的参数
    },
    {
        "url": "ssh://yidontekSW@192.168.101.93/volume1/GitRepo/SEMPro/SEM_DebugTools/ColumnClient.git",
        "branch": "",  # 留空 "" 则使用默认分支
        "local_name": "",  # 克隆到本地的目录名；留空则自动从 URL 提取
        "build_args": [],  # 额外传给 dotnet build 的参数
    },
    {
        "url": "ssh://yidontekSW@192.168.101.93/volume1/GitRepo/SEMPro/SEM_DebugTools/DetDebugTool.git",
        "branch": "",  # 留空 "" 则使用默认分支
        "local_name": "",  # 克隆到本地的目录名；留空则自动从 URL 提取
        "build_args": [],  # 额外传给 dotnet build 的参数
    },
    {
        "url": "ssh://yidontekSW@192.168.101.93/volume1/GitRepo/SEMPro/SEM_DebugTools/StageDebugTool.git",
        "branch": "",  # 留空 "" 则使用默认分支
        "local_name": "",  # 克隆到本地的目录名；留空则自动从 URL 提取
        "build_args": [],  # 额外传给 dotnet build 的参数
    },
]

# 全局配置
BASE_CLONE_DIR = Path("repos")  # 仓库统一克隆到此目录下
OUTPUT_BASE_DIR = Path("output")  # 编译产物输出根目录
DOTNET_CONFIGURATION = "Release"  # dotnet build -c 参数
SSH_KEY_PATH = ""  # SSH 私钥路径，留空则使用默认 (~/.ssh/id_rsa)
LOG_FILE = "build.log"  # 总日志文件名（位于 OUTPUT_BASE_DIR 下）


# ─────────────────────────────────────────────
# 工具函数
# ─────────────────────────────────────────────


class Logger:
    """同时向控制台和文件输出日志"""

    COLORS = {
        "RESET": "\033[0m",
        "BOLD": "\033[1m",
        "GREEN": "\033[92m",
        "YELLOW": "\033[93m",
        "RED": "\033[91m",
        "CYAN": "\033[96m",
        "DIM": "\033[2m",
    }

    def __init__(self, log_path: Path):
        log_path.parent.mkdir(parents=True, exist_ok=True)
        self._file = open(log_path, "a", encoding="utf-8")
        self._use_color = sys.stdout.isatty()

    def _c(self, color: str, text: str) -> str:
        if not self._use_color:
            return text
        return f"{self.COLORS.get(color, '')}{text}{self.COLORS['RESET']}"

    def _write(self, msg: str):
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._file.write(f"[{ts}] {msg}\n")
        self._file.flush()

    def info(self, msg: str):
        self._write(msg)
        print(self._c("CYAN", f"ℹ  {msg}"))

    def success(self, msg: str):
        self._write(f"✓ {msg}")
        print(self._c("GREEN", f"✓  {msg}"))

    def warning(self, msg: str):
        self._write(f"⚠ {msg}")
        print(self._c("YELLOW", f"⚠  {msg}"))

    def error(self, msg: str):
        self._write(f"✗ {msg}")
        print(self._c("RED", f"✗  {msg}"), file=sys.stderr)

    def header(self, msg: str):
        line = "─" * 60
        self._write(line)
        self._write(msg)
        self._write(line)
        print(self._c("BOLD", f"\n{line}\n  {msg}\n{line}"))

    def close(self):
        self._file.close()


def repo_name_from_url(url: str) -> str:
    """从 URL 提取仓库名（去掉 .git 后缀）"""
    name = url.rstrip("/").split("/")[-1]
    if name.endswith(".git"):
        name = name[:-4]
    return name


def build_git_env() -> dict:
    """构造 Git 使用的环境变量（可注入 SSH 私钥）"""
    env = os.environ.copy()
    if SSH_KEY_PATH:
        key = Path(SSH_KEY_PATH).expanduser()
        env["GIT_SSH_COMMAND"] = f"ssh -i {key} -o StrictHostKeyChecking=no"
    else:
        env["GIT_SSH_COMMAND"] = "ssh -o StrictHostKeyChecking=no"
    return env


def run(
    cmd: list[str], cwd: Path | None, log_file: Path, env: dict | None = None
) -> tuple[int, str]:
    """执行命令，实时打印并同时写入日志文件"""
    log_file.parent.mkdir(parents=True, exist_ok=True)
    output_lines = []

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"\n$ {' '.join(cmd)}\n")
        proc = subprocess.Popen(
            cmd,
            cwd=cwd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8",
            errors="replace",
            env=env,
        )
        for line in proc.stdout:  # type: ignore
            line_stripped = line.rstrip()
            output_lines.append(line_stripped)
            f.write(line)
            print(f"    {line_stripped}")
        proc.wait()

    return proc.returncode, "\n".join(output_lines)


# ─────────────────────────────────────────────
# 核心逻辑
# ─────────────────────────────────────────────


def clone_or_pull(repo: dict, logger: Logger, git_env: dict) -> tuple[bool, Path]:
    """克隆新仓库，或对已有仓库执行 git pull"""
    url = repo["url"]
    branch = repo.get("branch", "")
    local_name = repo.get("local_name", "") or repo_name_from_url(url)
    local_path = BASE_CLONE_DIR / local_name
    git_log = OUTPUT_BASE_DIR / local_name / "git.log"

    if local_path.exists():
        logger.info(f"[{local_name}] 目录已存在，执行 git pull …")
        cmd = ["git", "pull"]
        if branch:
            cmd += ["origin", branch]
        code, _ = run(cmd, cwd=local_path, log_file=git_log, env=git_env)
        if code != 0:
            logger.error(f"[{local_name}] git pull 失败（exit {code}）")
            return False, local_path
    else:
        logger.info(f"[{local_name}] 克隆仓库 {url} …")
        cmd = ["git", "clone", url, str(local_path)]
        if branch:
            cmd += ["--branch", branch]
        code, _ = run(cmd, cwd=None, log_file=git_log, env=git_env)
        if code != 0:
            logger.error(f"[{local_name}] git clone 失败（exit {code}）")
            return False, local_path

    logger.success(f"[{local_name}] Git 同步完成")
    return True, local_path


def build_repo(repo: dict, local_path: Path, logger: Logger) -> bool:
    """执行 dotnet build 并将产物输出到 output/<name>"""
    local_name = repo.get("local_name", "") or repo_name_from_url(repo["url"])
    out_dir = (OUTPUT_BASE_DIR / local_name).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    build_log = out_dir / "build.log"
    extra_args = repo.get("build_args", [])

    cmd = [
        "dotnet",
        "build",
        "-c",
        DOTNET_CONFIGURATION,
        f"--output={out_dir}",
        *extra_args,
    ]

    logger.info(f"[{local_name}] 开始编译 → {out_dir}")
    code, _ = run(cmd, cwd=local_path, log_file=build_log)

    if code != 0:
        logger.error(
            f"[{local_name}] dotnet build 失败（exit {code}），详见 {build_log}"
        )
        return False

    logger.success(f"[{local_name}] 编译成功，产物位于 {out_dir}")
    return True


def load_config(config_path: str) -> list[dict]:
    """从外部 JSON 文件加载仓库列表"""
    with open(config_path, encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, list):
        return data
    return data.get("repos", [])


# ─────────────────────────────────────────────
# 入口
# ─────────────────────────────────────────────


def main():
    parser = argparse.ArgumentParser(description="批量拉取 Git 仓库并 dotnet build")
    parser.add_argument("--config", help="外部 JSON 配置文件路径（可选）")
    parser.add_argument(
        "--only",
        nargs="+",
        metavar="NAME",
        help="只处理指定名称的仓库（空格分隔）",
    )
    parser.add_argument(
        "--skip-pull",
        action="store_true",
        help="跳过 git clone/pull，直接编译本地代码",
    )
    args = parser.parse_args()

    # 确定仓库列表
    repos = load_config(args.config) if args.config else DEFAULT_REPOS

    # 过滤仓库
    if args.only:
        repos = [
            r
            for r in repos
            if (r.get("local_name") or repo_name_from_url(r["url"])) in args.only
        ]
        if not repos:
            print("没有找到匹配的仓库，请检查 --only 参数。")
            sys.exit(1)

    OUTPUT_BASE_DIR.mkdir(parents=True, exist_ok=True)
    BASE_CLONE_DIR.mkdir(parents=True, exist_ok=True)

    log_path = OUTPUT_BASE_DIR / LOG_FILE
    logger = Logger(log_path)
    git_env = build_git_env()

    start = datetime.now()
    logger.header(
        f"开始批量构建  {start.strftime('%Y-%m-%d %H:%M:%S')}  共 {len(repos)} 个仓库"
    )

    results = {}  # name -> (git_ok, build_ok)

    for repo in repos:
        name = repo.get("local_name") or repo_name_from_url(repo["url"])
        logger.header(f"处理仓库：{name}")

        git_ok = True
        if not args.skip_pull:
            git_ok, local_path = clone_or_pull(repo, logger, git_env)
        else:
            local_path = BASE_CLONE_DIR / name
            if not local_path.exists():
                logger.error(f"[{name}] 本地目录不存在且已跳过 pull：{local_path}")
                results[name] = (False, False)
                continue

        if not git_ok:
            results[name] = (False, False)
            continue

        build_ok = build_repo(repo, local_path, logger)
        results[name] = (git_ok, build_ok)

    # ── 汇总报告 ──
    elapsed = datetime.now() - start
    logger.header(f"构建完成，耗时 {elapsed}")

    all_ok = True
    for name, (git_ok, build_ok) in results.items():
        if git_ok and build_ok:
            logger.success(f"{name:30s}  Git ✓  Build ✓")
        elif git_ok:
            logger.error(f"{name:30s}  Git ✓  Build ✗")
            all_ok = False
        else:
            logger.error(f"{name:30s}  Git ✗  Build ✗")
            all_ok = False

    logger.info(f"详细日志: {log_path}")
    logger.close()
    sys.exit(0 if all_ok else 1)


if __name__ == "__main__":
    main()
