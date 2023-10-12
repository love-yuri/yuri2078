if __name__ == "__main__":
  sum = 0 # 初始化和 
  i = 2 # 初始化起始变量

  # 开始循环
  while i <= 100 :
    sum += i # 累加sum
    i += 2 # 更新i的值

  # 打印i的值
  print("sum -> {}".format(sum))
