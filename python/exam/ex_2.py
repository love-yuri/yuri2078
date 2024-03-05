array = eval(input('请输入一个列表: '))
print(f'列表的和是 %d' % sum(array))

sorted_array = sorted(array, key=str)
reversed_array = sorted_array[::-1]
print(f'排序后的数组: {sorted_array}')
print(f'逆序排序后的数组: {reversed_array}')
print(f'和原数组是否相同: {array == reversed_array}')

print(f'最大值为: {max(array, key=str)}')
print(f'最小值为: {min(array, key=lambda x: len(str(x)))}')

print(f'元素的个数是: {len(array)}, 倒数第二个元素是: {array[-2]}')

input_str = input("请输入字符串：")

char_count = 0
digit_count = 0
space_count = 0
special_char_count = 0

for char in input_str:
    if char.isalpha(): 
        char_count += 1
    elif char.isdigit():  
        digit_count += 1
    elif char.isspace(): 
        space_count += 1
    else:
        special_char_count += 1

print("字符数量:", char_count)
print("数字数量:", digit_count)
print("空格数量:", space_count)
print("特殊字符数量:", special_char_count)

# 输入身份证号
id_card = input("请输入身份证号：")

birthday = id_card[6:14]
formatted_birthday = f"{birthday[0:4]}-{birthday[4:6]}-{birthday[6:8]}"

print("出生日期为:", formatted_birthday)

str = 'sdf, sdf2, 23'
print(f'字符串分割 {str.split(",")}')
print(f"字符串合并: {' '.join(['1', '2', '3'])}")

string = 'sfsdfsdf'
print(f'字符串切片: {string[:2]}')
print(f'sfds{string}')

