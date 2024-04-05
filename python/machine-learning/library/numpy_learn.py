'''
Author: love-yuri yuri2078170658@gmail.com
Date: 2024-04-05 22:35:57
LastEditTime: 2024-04-05 23:34:49
Description: numpy库学习
'''

import numpy as np
import inspect
from yuri_log import info, error

a = np.zeros(5) # 定义全是0的数组
b = np.ones(5) # 定义全是1的数组
# np.savetxt('a.txt', a) # 保存数据


info() << "全是0的数组: " << a
info() << "全是1的数组: " << b
