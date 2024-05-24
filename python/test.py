'''
Author: love-yuri yuri2078170658@gmail.com
Date: 2024-04-01 13:56:46
LastEditTime: 2024-05-24 20:07:45
Description: 自动将所有 /opt/apollo/neo/include 目录下的protobuf 头文件， 添加到系统include目录
'''

import numpy as np
import os 
from yuri_util import *

info() << Utils.get_script_dir(__file__)