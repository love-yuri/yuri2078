'''
Author: love-yuri yuri2078170658@gmail.com
Date: 2024-04-01 13:56:46
LastEditTime: 2024-05-21 13:50:30
Description: 自动将所有 /opt/apollo/neo/include 目录下的protobuf 头文件， 添加到系统include目录
'''
import sys

def get_package_location(package_name):
    package_location = None
    try:
        __import__(package_name)
        package_location = sys.modules[package_name].__file__
    except ImportError:
        print(f"Package '{package_name}' is not installed.")
    return package_location

package_name = 'numpy'  # 替换为你要查看位置的包的名称
location = get_package_location(package_name)
print(f"Package '{package_name}' is installed at: {location}")
