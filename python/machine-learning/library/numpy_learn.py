'''
Author: love-yuri yuri2078170658@gmail.com
Date: 2024-04-05 22:35:57
LastEditTime: 2024-04-18 21:16:12
Description: numpy库学习
'''

import numpy as np
import inspect
from yuri_log import info, error

# np.savetxt('a.txt', a) # 保存数据


info() << "全是0的数组: " << np.zeros(5) # 定义全是0的数组
info() << "全是1的数组: " << np.ones(5) # 定义全是1的数组

# 将数据复制， 可以是数字，也可以是元祖表示每个维度上重复的次数. 参数依次是每个维度
info() << "将((1,2), (3, 4)) 复制 2次 -> " << np.tile(((1,2), (3, 4)), 1)

# 默认整个求和， axis 设置求和方向， 0 沿着列求和， 1 沿着行求和
info() << "求和的结果 -> " << np.array([[1, 2], [3, 4]]).sum(axis=0)

# 返回排序后的索引值, 也就是从小到大的元素索引值
info() << "排序后的索引值 -> " << np.argsort([7, 2, 4, 3])

info() << "计算数组的平方 -> " << np.square(np.array([2, 2, 3, 4]))

info() << "计算数组的平方根 -> " << np.sqrt(np.array([4, 4, 9, 16]))

# 0是每列， 1 是每行
info() << "获取数据最小/大值 -> " << np.array([[4, 4, 9, 16], [1, 1, 10, 2]]).min(1)
