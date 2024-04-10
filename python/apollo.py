'''
Author: love-yuri yuri2078170658@gmail.com
Date: 2024-04-01 13:56:46
LastEditTime: 2024-04-09 09:00:07
Description: 自动将所有 /opt/apollo/neo/include 目录下的protobuf 头文件， 添加到系统include目录
'''
import os
import subprocess

rootPath = '/opt/apollo/neo/include'

class Protobuf:
  def __init__(self, path, file):
    self.path = path
    self.file = file
def find_proto_dir():
  directories = set()
  
  for root, dirs, files in os.walk(rootPath):
    for file in files:
      
      if file.endswith('.pb.h'):
        directories.add(Protobuf(root, file))

  return directories

# /opt/apollo/neo/include/cyber/proto
def cpToInclude():
  directories = find_proto_dir()
  for directory in directories:
    protobuf = directory.replace(rootPath, '', 1)
    # print(path)
    print(f'{protobuf.root}/{protobuf.file}')

cpToInclude()