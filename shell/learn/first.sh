#!/bin/bash
###
 # @Author: love-yuri yuri2078170658@gmail.com
 # @Date: 2024-04-08 20:23:46
 # @LastEditTime: 2024-04-09 09:11:17
 # @Description: 脚本学习
### 

allFile=$(ls -a) # 定义变量
# 循环变量
for file in $allFile; do
  # ${#str} 打印字符串长度
  echo "$file size -> ${#file}"
done

# 定义变量不能换行
a='hello '
b='world' 
# 拼接字符串
echo $a $b

str='this is a string'

# 字符串切割， 从下标 1 - 4, 如果 start > end
echo ${str:1:4}

