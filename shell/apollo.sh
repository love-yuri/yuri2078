#!/bin/bash
###
 # @Author: love-yuri yuri2078170658@gmail.com
 # @Date: 2024-04-08 20:25:38
 # @LastEditTime: 2024-04-09 21:59:54
 # @Description: apollo 脚本
### 

basePath="/opt/apollo/neo/include/"
targetPat="/usr/include/"

# 查找pb文件
result=$(sudo find "$basePath" -name "*.pb.h" | uniq)

# 输出结果
for item in $result; do
  oriPath=${item/$basePath}
  dirPath=$(dirname $oriPath)
  echo "sudo mkdir -p  ${targetPat}${dirPath}"
  echo "sudo cp ${item} ${targetPat}${oriPath}"
  sudo mkdir -p  "${targetPat}${dirPath}"
  sudo cp "${item}" "${targetPat}${oriPath}"
  
done

