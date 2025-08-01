import re

# 读取 load.sql 文件
def read_sql_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

# 解析 INSERT 语句
def parse_insert_statements(lines):
    insert_pattern = re.compile(r"INSERT INTO EOWDLog2 \(Uacc, Lens2Lsv, WD\) VALUES \((\d+\.?\d*), (-?\d+), (\d+)\);")
    data = []
    for line in lines:
        match = insert_pattern.match(line.strip())
        if match:
            uacc = float(match.group(1))  # 提取 Uacc
            lens2lsv = int(match.group(2))  # 提取 Lens2Lsv
            wd = int(match.group(3))  # 提取 WD
            data.append((uacc, wd, lens2lsv, line.strip()))  # 保存为元组
    return data

# 检查重复并去重
def check_and_remove_duplicates(data):
    unique_dict = {}  # 用于存储唯一的 (Uacc, WD) 组合
    for item in data:
        uacc, wd, lens2lsv, line = item
        key = (uacc, wd)  # 以 (Uacc, WD) 为键

        if key in unique_dict:
            # 如果 (Uacc, WD) 已存在，检查 Lens2Lsv 是否相同
            existing_lens2lsv = unique_dict[key][0]
            if existing_lens2lsv != lens2lsv:
                raise ValueError(f"错误: (Uacc, WD){existing_lens2lsv} {lens2lsv} 重复但 Lens2Lsv 不同: {line}")
        else:
            # 如果 (Uacc, WD) 不存在，添加到字典
            unique_dict[key] = (lens2lsv, line)
    
    # 返回去重后的数据
    return [value[1] for value in unique_dict.values()]

# 按 Uacc 和 WD 排序
def sort_data(data):
    # 先按 Uacc 排序，再按 WD 排序
    return sorted(data, key=lambda x: (x[0], x[1]))

# 生成新的 load2.sql 文件
def generate_sql_file(data, output_path):
    with open(output_path, 'w') as file:
        for line in data:
            file.write(line + '\n')  # 写入去重后的 INSERT 语句

# 主函数
def main():
    input_file = 'load.sql'
    output_file = 'load2.sql'

    try:
        # 读取文件
        lines = read_sql_file(input_file)
        
        # 解析 INSERT 语句
        data = parse_insert_statements(lines)
        
        print(f"已解析 INSERT 语句: {len(data)}")

        # 去重并检查 Lens2Lsv
        unique_data = check_and_remove_duplicates(data)
        print(f"已去重并检查 Lens2Lsv: {len(data)} -> {len(unique_data)}")

        # 按 Uacc 和 WD 排序
        sorted_data = sort_data([(item[0], item[1], item[2], item[3]) for item in (parse_insert_statements(unique_data))])

        # 生成新的 SQL 文件
        generate_sql_file([item[3] for item in sorted_data], output_file)
        print(f"已生成去重并排序后的 SQL 文件: {output_file}")
    except ValueError as e:
        print(e)

# 运行主函数
if __name__ == "__main__":
    main()