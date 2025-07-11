'''
Author: love-yuri yuri2078170658@gmail.com
Date: 2025-03-26 11:48:33
LastEditTime: 2025-07-03 13:36:57
Description: 
'''
from typing import Tuple
import math
import sqlite3
import pandas as pd

file_path = "C:\\Users\\love-yuri\\Documents\\work\\亮度对比度pmt采集.xlsx"

# 读取 Excel 文件


def read_excel(file_path=file_path):
  # 使用 pandas 读取 Excel 文件
  df = pd.read_excel(file_path)
  apIndexMap = {
      '10': 1,
      '15': 3,
      '20': 4,
      '30': 5,
      '60': 6,
      '120': 7
  }

  def to_float(data):
    try:
      value = float(str(data).strip())
      if math.isnan(value):
        return 0.0
      return value
    except:
      return 0.0
  data: list[DetPMT] = []
  with open("load.sql", "+w") as file:
    # 逐行输出第 2 列和第 5 列的内容
    for index, row in df.iterrows():
      vac = float(row.iloc[1] * 1000)
      apIndex = apIndexMap.get(str(row.iloc[3]), 5)
      wd = float(row.iloc[4])
      et = to_float(row.iloc[5])
      inlens = to_float(row.iloc[7])
      type = row.iloc[2]
      if not str(type).strip().startswith('normal'):
        continue
      det = DetPMT(
          vac=vac,
          wd=wd,
          apIndex=apIndex,
          et=et,
          inlens=inlens
      )
      data.append(det)
      if det.apIndex == 1:
        data.append(
            DetPMT(
                vac=det.vac,
                wd=det.wd,
                apIndex=2,
                et=det.et,
                inlens=det.inlens
            )
        )
      # print(f'vac: {vac}, apIndex: {apIndex}, wd: {wd}, et: {et}, inlens: {inlens}')
    return data


class DetPMT:
  def __init__(self, vac: float, wd: float, apIndex: int, et: float, inlens: float):
    self.vac = vac
    self.wd = wd
    self.apIndex = apIndex
    self.et = et
    self.inlens = inlens


def connect():
  con = sqlite3.connect("E:\\work\\database\\EO.s3db")
  data = con.execute('select * from DetPMT order by Uacc, WD, ApIndex;')

  full_sql_data: dict[Tuple[float, float, int], DetPMT] = {}
  for excel_data in read_excel():
    key = (excel_data.vac, excel_data.wd, excel_data.apIndex)
    if excel_data.et == 0.0 or excel_data.inlens == 0.0:
      continue
    full_sql_data[key] = excel_data

  for row in data.fetchall():
    key = (row[0], row[1], row[2])
    if key in full_sql_data:
      # print(f'{key} 已经存在')？
      pass
    elif row[3] != 0.0 and row[4] != 0.0:
      full_sql_data[key] = DetPMT(
          vac=row[0],
          wd=row[1],
          apIndex=row[2],
          et=row[3],
          inlens=row[4]
      )

  full_sql_data = dict(sorted(full_sql_data.items(), key=lambda item: item[0]))

  with open('eo.sql', 'w', encoding='utf-8') as file:
    for key, data in full_sql_data.items():
      file.write(
          f'INSERT INTO DetPMT (Uacc, WD, ApIndex, ETPMTLsv, InlensPMTLsv) VALUES ({data.vac}, {data.wd}, {data.apIndex}, {data.et}, {data.inlens});\n')
      print(
          f'vac: {key[0]}, wd: {key[1]}, apIndex: {key[2]}, et: {data.et}, inlens: {data.inlens}')

  print(f'size: {full_sql_data.__len__()}')


# 主程序
if __name__ == "__main__":
  connect()
