file_path = "csv/money.txt"

with open(file_path, 'r') as file:
    zhen = 0
    fu = 0
    for line in file:
        try:
            number = float(line.strip().replace(",", ""))  # 将每行内容转换成浮点数
            if(number > 0 and number < 10000) :
                zhen = zhen + number
            else :
                fu = fu - number
            # print(number)
        except ValueError:
            print(f"Cannot convert '{line.strip()}' to a number.")  # 如果无法转换成数字，则打印错误消息
    print(f'收入: {zhen}元, 支出: {fu}元')