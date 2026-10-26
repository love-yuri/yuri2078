import sys
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Optional


INPUT_FILE = Path(__file__).with_name("pmt.txt")
HEADER = ("电压", "WD", "光阑", "ET-PMT", "Inlens-PMT")
AP_INDEX_MAP = {
  Decimal("10"): (1, 2),
  Decimal("15"): (3,),
  Decimal("20"): (4,),
  Decimal("30"): (5,),
  Decimal("60"): (6,),
  Decimal("120"): (7,),
}


@dataclass
class DetPMT:
  line_no: int
  uacc: Decimal
  wd: Decimal
  ap_index: int
  et: Optional[Decimal]
  inlens: Optional[Decimal]


def format_decimal(value: Decimal) -> str:
  if value == 0:
    return "0"
  return format(value.normalize(), "f")


def parse_decimal(text: str, line_no: int, field_name: str) -> Decimal:
  try:
    return Decimal(text)
  except InvalidOperation as e:
    raise ValueError(f"第 {line_no} 行 {field_name} 不是数字：{text}") from e


def parse_nullable_decimal(text: str, line_no: int, field_name: str) -> Optional[Decimal]:
  if text == "/":
    return None
  return parse_decimal(text, line_no, field_name)


def get_ap_indexes(aperture: Decimal, line_no: int) -> tuple[int, ...]:
  ap_indexes = AP_INDEX_MAP.get(aperture)
  if ap_indexes is None:
    values = ", ".join(format_decimal(value) for value in AP_INDEX_MAP)
    raise ValueError(f"第 {line_no} 行 光阑不支持：{format_decimal(aperture)}，支持值：{values}")
  return ap_indexes


def parse_line(line: str, line_no: int) -> list[DetPMT]:
  parts = line.split()
  if len(parts) != 5:
    raise ValueError(f"第 {line_no} 行格式错误：需为 '电压 WD 光阑 ET-PMT Inlens-PMT' -> {line.rstrip()}")

  voltage_text, wd_text, aperture_text, et_text, inlens_text = parts
  uacc = parse_decimal(voltage_text, line_no, "电压") * Decimal("1000")
  wd = parse_decimal(wd_text, line_no, "WD")
  aperture = parse_decimal(aperture_text, line_no, "光阑")
  et = parse_nullable_decimal(et_text, line_no, "ETPMTLsv")
  inlens = parse_nullable_decimal(inlens_text, line_no, "InlensPMTLsv")

  records = []
  for ap_index in get_ap_indexes(aperture, line_no):
    records.append(
      DetPMT(
        line_no=line_no,
        uacc=uacc,
        wd=wd,
        ap_index=ap_index,
        et=et,
        inlens=inlens,
      )
    )
  return records


def nearest_record(record: DetPMT, records: list[DetPMT]) -> DetPMT:
  candidates = [
    item for item in records
    if item.ap_index == record.ap_index
    and item.et is not None
    and item.inlens is not None
  ]
  if not candidates:
    raise ValueError(f"第 {record.line_no} 行 ApIndex={record.ap_index} 找不到可用于补齐的数据")

  return min(
    candidates,
    key=lambda item: (
      abs(item.wd - record.wd),
      abs(item.uacc - record.uacc),
      item.line_no,
    ),
  )


def fill_missing_values(records: list[DetPMT]) -> None:
  for record in records:
    if record.et is not None and record.inlens is not None:
      continue

    nearest = nearest_record(record, records)
    if record.et is None:
      record.et = nearest.et
    if record.inlens is None:
      record.inlens = nearest.inlens


def to_sql(record: DetPMT) -> str:
  if record.et is None or record.inlens is None:
    raise ValueError(f"第 {record.line_no} 行补齐失败")

  return (
    "insert into DetPMT (Uacc, WD, ApIndex, ETPMTLsv, InlensPMTLsv) "
    f"VALUES ({format_decimal(record.uacc)}, {format_decimal(record.wd)}, {record.ap_index}, "
    f"{format_decimal(record.et)}, {format_decimal(record.inlens)});"
  )


def main() -> None:
  try:
    lines = INPUT_FILE.read_text(encoding="utf-8-sig").splitlines()
    if not lines:
      raise ValueError(f"{INPUT_FILE} 没有内容")

    header = tuple(lines[0].split())
    if header != HEADER:
      raise ValueError(f"第 1 行表头错误：期望 {' '.join(HEADER)} -> {lines[0].rstrip()}")

    records = []
    for line_no, line in enumerate(lines[1:], start=2):
      if not line.strip():
        continue
      records.extend(parse_line(line, line_no))

    fill_missing_values(records)
    print("\n".join(to_sql(record) for record in records))
  except Exception as e:
    print(e, file=sys.stderr)
    sys.exit(1)


if __name__ == "__main__":
  main()
