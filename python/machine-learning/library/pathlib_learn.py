import pathlib
from yuri_util import *

# 创建一个路径对象
path = pathlib.Path('D:\\love-yuri\\yuri2078\\python\\machine-learning\\knn\\teset')

for file in path.iterdir():
  if file.is_file():
    info() << "File: " << file.name
  else:
    p = pathlib.Path(file)
    for i in p.iterdir():
      if i.is_file():
        info() << "File2: " << i.name