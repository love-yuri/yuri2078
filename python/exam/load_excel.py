import pandas as pd

# 读取 Excel 文件
def read_excel(file_path):
  # 使用 pandas 读取 Excel 文件
  df = pd.read_excel(file_path)
  
  with open("load.sql", "+w") as file:
    # 逐行输出第 2 列和第 5 列的内容
    for index, row in df.iterrows():
      wd = round(row.iloc[0])
      v = round(row.iloc[1] / 1000)
      lens2 = round(row.iloc[2])
      file.write(f"INSERT INTO EOWDLog2 (Uacc, Lens2Lsv, WD) VALUES ({v}, {lens2}, {wd});\n")
      print(f"wd: {row.iloc[0]:.0f}, v: {(row.iloc[1]/1000):.0f}, lens2: {row.iloc[2]:.0f}")

# 主程序
if __name__ == "__main__":
  # 替换为你的 Excel 文件路径
  file_path = "C:\\Users\\love-yuri\\Documents\\work\\工作簿1.xlsx"
  read_excel(file_path)