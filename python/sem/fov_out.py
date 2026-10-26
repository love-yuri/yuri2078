"""
Author: love-yuri yuri2078170658@gmail.com
Date: 2026-06-03 11:12:42
LastEditTime: 2026-06-03 11:12:44
Description:
"""

import argparse
import re
import sys


LINE_RE = re.compile(r"^(\d+)\s*[kK][vV]$")

def parse_line(line: str, line_no: int):
  text = line.strip()
  if not text:
    return None  # 跳过空行

  parts = text.split()
  if len(parts) != 4:
    raise ValueError(
      f"第 {line_no} 行解析失败：应为4列，当前为 {len(parts)} 列 -> {line.rstrip()}"
    )

  eth_part, scale_2, scale_3, scale_4 = parts

  m = LINE_RE.match(eth_part)
  if not m:
    raise ValueError(
      f"第 {line_no} 行解析失败：EHT格式不合法，需类似 5kv -> {eth_part}"
    )

  eht = m.group(1)  # 5kv -> 5

  scales = [scale_2, scale_3, scale_4]
  for s in scales:
    try:
      float(s)
    except ValueError:
      raise ValueError(f"第 {line_no} 行解析失败：倍率不是合法数字 -> {s}")

  return [
    f"update FOVConfig set FOV = FOV * {scale_2} where EHT = {eht} and MagRange = 2;",
    f"update FOVConfig set FOV = FOV * {scale_3} where EHT = {eht} and MagRange = 3;",
    f"update FOVConfig set FOV = FOV * {scale_4} where EHT = {eht} and MagRange = 4;",
  ]


def main():
  parser = argparse.ArgumentParser(
    description="Parse kv lines and generate FOVConfig SQL"
  )
  parser.add_argument("input_file", nargs="?", help="输入文件路径", default='/home/yuri/love-yuri/yuri2078/python/sem/test.txt')
  parser.add_argument(
    "output_file",
    nargs="?",
    default="output.sql",
    help="输出SQL文件（默认 output.sql）",
  )
  args = parser.parse_args()

  statements = []

  try:
    with open(args.input_file, "r", encoding="utf-8") as f:
      for i, line in enumerate(f, start=1):
        parsed = parse_line(line, i)
        if parsed is not None:
          statements.extend(parsed)
  except Exception as e:
    print(f"读取文件失败：{e}", file=sys.stderr)
    sys.exit(1)

  # 解析成功才写文件
  try:
    with open(args.output_file, "w", encoding="utf-8") as f:
      f.write("\n".join(statements))
    print(f"生成成功：{args.output_file}")
  except Exception as e:
    print(f"写入文件失败：{e}", file=sys.stderr)
    sys.exit(1)


if __name__ == "__main__":
  main()
