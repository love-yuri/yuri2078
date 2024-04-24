'''
Author: love-yuri yuri2078170658@gmail.com
Date: 2024-04-05 23:03:15
LastEditTime: 2024-04-18 20:21:24
Description: python工具
'''
import os
import sys
import time
import threading
from builtins import open


mutex = threading.Lock()
write_in_file = False  # 是否写入文件

def log_result(msg, output=sys.stdout):
  print(msg, file=output)

def set_write_in_file():
  global write_in_file
  write_in_file = True

class Log:
  def __init__(self, line, is_error=False):
    self.ost = []
    if is_error and not write_in_file:
      self.ost.append("\x1b[31m")

    current_time = time.strftime("%H:%M:%S", time.localtime())
    self.ost.append(f"{current_time} line:{line} -> ")
    
  def __del__(self):
    mutex.acquire()
    try:
      if write_in_file:
        try:
          with open("log.txt", "a") as f:
            log_result("".join(self.ost), output=f)
        except Exception as e:
          print(e)
      else:
        self.ost.append("\x1b[0m")
        log_result("".join(self.ost))
    finally:
      mutex.release()

  def __lshift__(self, val):
    self.ost.append(str(val))
    return self


def info():
  return Log(sys._getframe().f_back.f_lineno)

def error():
  return Log(sys._getframe().f_back.f_lineno, is_error=True)

def get_script_dir(file) -> str:
  return os.path.dirname(os.path.realpath(file))