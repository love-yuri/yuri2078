# -*- coding: utf-8 -*-

import sys
import tty
import termios
import os
import tf
import rospy
from dobot.srv import GetPose

def get_char():
  # 获取当前终端设置
  old_settings = termios.tcgetattr(sys.stdin)
  try:
    # 将终端设置修改为不需要回车键确认
    tty.setcbreak(sys.stdin.fileno())

    # 从标准输入读取一个字符
    char = sys.stdin.read(1)
  finally:
    # 恢复原始的终端设置
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
  return char

def getCurrentPos():
  try:
    (trans,rot) = tf_listener.lookupTransform('map', 'base_link', rospy.Time(0)) 
    x,y,z = trans[0], trans[1], trans[2]
    x_,y_,z_, w = rot[0], rot[1], rot[2], rot[3]
    rospy.loginfo("pos -> {}, {}, {}, {}, {}, {}, {}".format(x,y,z, x_,y_, z_, w))
  except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException) as e: 
    rospy.logerr('发生错误！！ %s', e)

def getDobotPos():
  try:
    # 调用服务，等待响应
    response = dobot_client()
    print("call dobot success! -> {}".format(response))
  except rospy.ServiceException as e:
    rospy.logerr("服务调用失败: %s", e)
  

def main():
  # 初始化ros节点
  rospy.init_node('get_params')
  # 订阅位置信息
  global tf_listener, dobot_client
  tf_listener = tf.TransformListener() 
  dobot_client = rospy.ServiceProxy('/DobotServer/GetPose', GetPose)
  rospy.loginfo("初始化成功, 功能列表")
  rospy.loginfo("1: 获取当前小车的位置")
  rospy.loginfo("2: 获取当前机械臂的位置")
  while True:
    choice = get_char()
    if choice == '1':
      getCurrentPos()
    elif choice == '2':
      getDobotPos()
    else:
      break

    sys.stdout.flush()

if __name__ == "__main__":
  main()
