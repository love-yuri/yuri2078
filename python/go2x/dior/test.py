import csv

# 定义CSV文件路径
csv_file_path = "csv/护肤.csv"

# 读取CSV文件
with open(csv_file_path, newline='') as csvfile:
    reader = csv.reader(csvfile)
    # 读取每一行数据
    for row in reader:
        print(', '.join(row))  # 打印每一行数据
