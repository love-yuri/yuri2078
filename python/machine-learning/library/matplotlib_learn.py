'''
Author: love-yuri yuri2078170658@gmail.com
Date: 2024-05-21 14:38:37
LastEditTime: 2024-05-21 21:01:51
Description: python matplotlib 学习
'''
import matplotlib.pyplot as plt
import numpy as np

# plt.plot(xpoint, ypoint, args)
# xpoint: 数据点x坐标
# ypoint: 数据点y坐标
# args: 格式化字符串，用于指定数据点的样式，如颜色、形状等


points = [(1, 3), (2, 4), (3, 1), (4, 2)]
x = [point[0] for point in points]
y = [point[1] for point in points]

################### 创建图标 ###################

# 创建一个画布， num=1 表示使用第一个画布， figsize=(6,6) 表示画布大小为6x6
fig = plt.figure(num=1,figsize=(12,6))

## 创建一个子图，111 表示子图的布局
# 111： 表示将画布分为1行1列，1：表示第一个子图

# 防止中文标题显示错误
plt.rcParams["font.family"]="SimHei"


ax = fig.add_subplot(121)
ax.set_title('中文')
ax.plot(x, y, 'o', label='Data Points')
ax.legend(loc=1,labelspacing=1,handlelength=1,fontsize=14,shadow=True)
ax.plot(y,x, 'o', label='Data Points')
ax.legend(loc=1,labelspacing=1,handlelength=1,fontsize=14,shadow=True)
ax.set_xticklabels(['a', 'b', 'c', 'd'], fontproperties="SimHei", fontsize=12, color='red')
ax = fig.add_subplot(122)
ax.set_title('Line Plot')
ax.plot(x, y, '-')

## 显示图表
plt.show()