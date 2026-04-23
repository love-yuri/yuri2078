import os
import re
import sys
import subprocess

# 工作目录 支持递归
working_directory = r"E:\work"

# 目标ip
target_ip = "10.0.1.152"


def process_run(cmd: str, args: str = "", work_path: str = "") -> str:
  """执行命令并获取输出"""
  if not work_path or not os.path.isdir(work_path):
    raise FileNotFoundError(f"工作目录不存在: {work_path}")

  result = subprocess.run(
    [cmd, *args.split()],
    cwd=work_path,
    capture_output=True,
    text=True,
    encoding="utf-8",
    errors="ignore",
  )

  if result.returncode != 0:
    raise RuntimeError(f"命令执行失败 (退出码: {result.returncode}): {result.stderr}")

  return result.stdout.strip()


def is_git_repo_root(path: str) -> bool:
  """判断该目录是否为 git 仓库根目录（包括 submodule）"""
  git_path = os.path.join(path, ".git")
  # 普通仓库: .git 是目录; submodule: .git 是文件
  if not os.path.exists(git_path):
    return False
  try:
    toplevel = process_run("git", "rev-parse --show-toplevel", path)
    return os.path.normpath(toplevel) == os.path.normpath(path)
  except Exception:
    return False


def run():
  """执行 remote 切换"""
  for root, dirs, _ in os.walk(working_directory):
    # 跳过隐藏目录
    dirs[:] = [d for d in dirs if not d.startswith(".")]

    # 仅处理真正的 git 仓库根目录（含 submodule）
    if not is_git_repo_root(root):
      continue

    try:
      info = process_run("git", "remote -v", root)
    except Exception as e:
      print(f"[{root}] 执行 git remote -v 失败: {e}", file=sys.stderr)
      continue

    remote_regex = re.compile(r"(ssh://yidontekSW[^ ]+)")
    match = remote_regex.search(info)
    if match:
      remote = match.group(1)
      new_remote = re.sub(r"\d+\.\d+\.\d+\.\d+", target_ip, remote)
      try:
        process_run("git", f"remote set-url origin {new_remote}", root)
        print(f"remote: {root} 处理完毕")
      except Exception as e:
        print(f"[{root}] 设置 remote 失败: {e}", file=sys.stderr)
    else:
      print(f"{root} 无匹配 remote，跳过", file=sys.stderr)


if __name__ == "__main__":
  run()
