'''
Author: love-yuri yuri2078170658@gmail.com
Date: 2026-06-08 16:37:51
LastEditTime: 2026-06-09 09:11:40
Description: 
'''
import re
import sys
from decimal import Decimal


INPUT_TEXT = """5wd   10kv          224.3    209.1
5wd   11kv                 224.0    208.2
5wd   12kv                 223.7    208.5
5wd   13kv                 176.3    207.7
5wd   14kv                 175.5    208.7
5wd   15kv                 224.6    209.4
5wd   16kv                175.3     208.3
5wd   17kv                175.3     208.8
5wd   18kv                175.0     209.0
5wd   19kv                175.0     209.8
5wd   20kv                224.9     210.4
5wd   9kv                  224.9     209.5
5wd   8kv                  223.8     209.1     
5wd   7kv                  224.1     209.8
5wd   6kv                 224         209.8
5wd   5kv                 223.8     209.9
5wd   4kv                 222.8     210.8
5wd   3kv                220.8      211.7
5wd   2kv                219.9     225.1
5wd   1kv                202.7     222.1
6wd 1kv   191.8     230.2
6wd 2kv   210.8     217.4
6wd 3kv   218.5      214.3
6wd 4kv   220.5     212.6
6wd 5kv    221.3    212.8
6wd 6kv     222.0    211.5
6wd 7kv      222.1      210.9
6wd 8kv    221.8      211.1
6wd 9kv    222.8      211.2
6wd  10kv     222.8    210.5
6wd  11kv     221.8    210.6
7wd 10kv   220.3   212.1
7wd 9kv     221.0   212.3
7wd 8kv     220.4   213.3
7wd 7kv     220.3   213.2
7wd 6kv     220.2   213.3
7wd 5kv     219.1   213.8
7wd 4kv     218.0   214.7
7wd 3kv     216.0   216.0
7wd 2kv     206      219.9
7wd 1kv     191.8   239.2 
8wd 10kv   219.3  213.4
8wd 9kv     219.5  213.3
8wd 8kv    218.4   214.2
8wd 7kv    218.8   214.4
8wd 6kv    218.2   214.7
8wd 5kv    217.6   217.6
8wd 4kv    216.1   216.1
8wd 3kv    213.5   218.6
8wd 2kv    199.8   224.0
8wd 1kv    191.8   255.7
9wd 10kv   217.8    215.5
9wd 9kv    217.9    217.9
9wd 8kv    216.8    216.8
9wd 7kv    216.8    216.8
9wd 6kv    215.7    215.7
9wd 5kv    215.2    215.2
9wd 4kv    213.9    219.2
9wd 3kv    211.1    221.7
9wd 2kv    199.8    228.4
10wd 10kv  215.8   215.8
10wd 9kv   216.4   216.4
10wd 8kv   215.3   215.3
10wd 7kv   215.2   215.2
10wd 6kv   214.2   218.2
10wd 5kv   213.6   219
10wd 4kv   211.1   220.6
10wd 3kv   208.2   224.4
10wd 2kv   199.8   233.6
4wd 10kv   226.8   206.5
4wd 9kv    227.1  207.8
4wd 8kv    227.4  207.4
4wd 7kv    226.8  206.9
4wd 6kv    226.6  207.6
4wd 5kv    226.5  206.9
4wd 4kv    225.8  207.7
4wd 3kv    224.1  206.4
4wd 2kv    223.5  210.5
4wd 1kv    215.8  215.8
4wd 11kv   225.7  206
4wd 12kv   225.6 206.6
4wd 13kv   177.5 206.6
4wd 14kv   177.2  206.4
4wd 15kv   246.2  208.0
4wd 16kv   176.9  207.2
4wd 17kv   176.9  205.7
4wd 18kv   176.7  206.6
4wd 19kv   176.3  208.1
4wd 20kv   227.1  207.3
3wd 10kv  229.3  204.4
3wd 9kv   229.6  205.4
3wd 8kv   229.4  205.3
3wd 7kv   229.2  203.5
3wd 6kv   229.1  204.9
3wd 5kv   229.0   205.2
3wd 4kv   228.7   205
3wd 3kv   227.5   205.5
3wd 2kv   227.3  206.6
3wd 1kv  223.5    208.9"""


LINE_RE = re.compile(
  r"^\s*([+-]?\d+(?:\.\d+)?)\s*[wW][dD]\s+([+-]?\d+(?:\.\d+)?)\s*[kK][vV]\s+([+-]?\d+(?:\.\d+)?)\s+([+-]?\d+(?:\.\d+)?)\s*$"
)


def format_decimal(value: Decimal) -> str:
  if value == 0:
    return "0"
  return format(value.normalize(), "f")


def parse_line(line: str, line_no: int) -> str:
  match = LINE_RE.match(line)
  if not match:
    raise ValueError(
      f"第 {line_no} 行格式错误：需为 '[wd]wd [hv]kv origin new' -> {line.rstrip()}"
    )

  wd_text, hv_text, origin_text, new_text = match.groups()
  wd = Decimal(wd_text)
  uacc = Decimal(hv_text)
  origin = Decimal(origin_text)
  new = Decimal(new_text)
  dis = new - origin

  return (
    "update CalibrationAngle set Angle = Angle - "
    f"{format_decimal(dis)} where WD = {format_decimal(wd)} "
    f"and Uacc = {format_decimal(uacc)};"
  )


def main() -> None:
  try:
    lines = INPUT_TEXT.splitlines()
    if not lines:
      raise ValueError("INPUT_TEXT 没有内容")

    statements = [parse_line(line, i) for i, line in enumerate(lines, start=1)]
    print("\n".join(statements))
  except Exception as e:
    print(e, file=sys.stderr)
    sys.exit(1)


if __name__ == "__main__":
  main()
