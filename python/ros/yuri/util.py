# -*- coding: utf-8 -*-

import sys
import tty
import termios
import os
import time
import tf
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from geometry_msgs.msg import Pose, Point, Quaternion
from dobot.srv  import *
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import PoseWithCovarianceStamped
from move_base_msgs.msg import MoveBaseActionResult
from geometry_msgs.msg import PoseWithCovarianceStamped
from geometry_msgs.msg import Twist

global step
step = 0
testFlag = 1 # 是否是开发环境

# 初始化位置
def initPos(pos):
  global initialpose_pub, amcl_pose_pub
  amcl_pose_pub.publish(pos)
  initialpose_pub.publish(pos)
  

# 初始化位置的 位置信息
def InitPosVal(a,b,c,d,e,f,g):
    pose_msg = PoseWithCovarianceStamped()
    pose_msg.header.frame_id = 'map'
    pose_msg.header.stamp = rospy.Time.now()
    pose_msg.pose.pose.position.x = a
    pose_msg.pose.pose.position.y = b
    pose_msg.pose.pose.position.z = c
    pose_msg.pose.pose.orientation.x = d
    pose_msg.pose.pose.orientation.y = e
    pose_msg.pose.pose.orientation.z = f
    pose_msg.pose.pose.orientation.w = g
    return pose_msg

# 导航点的位置信息
def MapPosVal(a,b,c,d,e,f,g):
    pose_msg = PoseStamped()
    pose_msg.header.frame_id = 'map'
    pose_msg.pose.position.x = a
    pose_msg.pose.position.y = b
    pose_msg.pose.position.z = c
    pose_msg.pose.orientation.x = d
    pose_msg.pose.orientation.y = e
    pose_msg.pose.orientation.z = f
    pose_msg.pose.orientation.w = g
    return pose_msg


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
    formatted_x = "{:.11f}".format(x) if len(str(x).split('.')[1]) >= 11 else str(x)
    formatted_y = "{:.11f}".format(y) if len(str(y).split('.')[1]) >= 11 else str(y)
    formatted_z = "{:.11f}".format(z) if len(str(z).split('.')[1]) >= 11 else str(z)
    formatted_x_ = "{:.11f}".format(x_) if len(str(x_).split('.')[1]) >= 11 else str(x_)
    formatted_y_ = "{:.11f}".format(y_) if len(str(y_).split('.')[1]) >= 11 else str(y_)
    formatted_z_ = "{:.11f}".format(z_) if len(str(z_).split('.')[1]) >= 11 else str(z_)
    formatted_w = "{:.11f}".format(w) if len(str(w).split('.')[1]) >= 11 else str(w)


    rospy.loginfo("pos -> %s, %s, %s, %s, %s, %s, %s", formatted_x, formatted_y, formatted_z, formatted_x_, formatted_y_, formatted_z_, formatted_w)
    return InitPosVal(x, y, z, x_, y_, z_, w)
  except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException) as e: 
    rospy.logerr('发生错误！！ %s', e)

def getDobotPos():
  try:
    # 调用服务，等待响应
    res = dobot_client()
    x = res.x
    y = res.y
    z = res.z
    r = res.r
    result = res.result

    x = "{:.11f}".format(x) if len(str(x).split('.')[1]) >= 11 else str(x)
    y = "{:.11f}".format(y) if len(str(y).split('.')[1]) >= 11 else str(y)
    z = "{:.11f}".format(z) if len(str(z).split('.')[1]) >= 11 else str(z)
    r = "{:.11f}".format(r) if len(str(r).split('.')[1]) >= 11 else str(r)

    rospy.loginfo("dobot -> %s, %s, %s, %s, %s", result, x, y, z, r)
  except rospy.ServiceException as e:
    rospy.logerr("服务调用失败: %s", e)

def read_pos_file(row):
  try:
    n = 0
    with open('/home/eaibot/yuri/pos.txt', 'r') as file:
      for line in file.readlines():
        n = n + 1
        if n != row:
          continue
        line = line.replace('\n', '')
        # line = file.readline().strip()
        numbers = line.split(',')
        if len(numbers) != 7:
          raise ValueError("文件内容不符合要求，应该包含 7 个数字, 以逗号分1隔")

        # 将字符串转换为浮点数
        x = float(numbers[0])
        y = float(numbers[1])
        z = float(numbers[2])
        x_ = float(numbers[3])
        y_ = float(numbers[4])
        z_ = float(numbers[5])
        w = float(numbers[6])

        return x, y, z, x_, y_, z_, w
  except Exception as e:
    print("读取文件失败:", e)
    return None

def pose_callback(msg):
    if msg.status.status == 3: 
      rospy.loginfo("导航成功!!!, 正在初始化位置!!")
      initPos(getCurrentPos())
      time.sleep(1)
      # move(20)
      rospy.loginfo("初始化位置成功!!")

def openSuck():
  global suck_client
  suck_client(1, 1, False) # open suck

def closeSuck():
  global suck_client
  suck_client(1, 0, False) # open suck

def dh(row):
  rospy.loginfo('正在导航..........')
  global step
  step = 1
  turtle_vel_pub.publish(PoseStamped()) 
  time.sleep(1)
  rospy.Subscriber('/move_base/result', MoveBaseActionResult, pose_callback) 
  x, y, z, x_, y_, z_, w = read_pos_file(row)
  turtle_vel_pub.publish(MapPosVal(x, y,z, x_, y_, z_, w))

def move(distance):
  global move_client
  twist = Twist()
  twist.linear.x = distance; twist.linear.y = 0; twist.linear.z = 0;
  twist.angular.x = 0; twist.angular.y = 0; twist.angular.z = 0
  move_client.publish(twist)

def moveDoBot():
  n = 0
  
  with open("dobot.txt", "r") as file:
    for line in file:
      n = n + 1
      # 去除行末的换行符并按逗号分隔
      numbers = line.strip().split(',')
      
      # 检查是否有5个数字
      if len(numbers) != 5:
        break
      
      # 将字符串转换为浮点数
      num1 = float(numbers[0])
      num2 = float(numbers[1])
      num3 = float(numbers[2])
      num4 = float(numbers[3])
      num5 = float(numbers[4])

      global arm_client
      rospy.loginfo("正在导航机械臂....%f %f %f %f %f", num1, num2, num3, num4, num5)
      arm_client(num1, num2, num3, num4, num5)
      time.sleep(5)
      if n == 2:

        openSuck()
        # start_time = time.time()
        # while time.time() - start_time <= 2 :
        #   move(0.3)
        # time.sleep(2)
      if n == 3:
        closeSuck()
        rospy.loginfo('正在导航..........')
        turtle_vel_pub.publish(PoseStamped()) 
        time.sleep(1)
        rospy.Subscriber('/move_base/result', MoveBaseActionResult, pose_callback_test) 
        x, y, z, x_, y_, z_, w = read_pos_file(2)
        turtle_vel_pub.publish(MapPosVal(x, y,z, x_, y_, z_, w))

def moveDoBot2():
  n = 0
  with open("dobot2.txt", "r") as file:
    for line in file:
      n = n + 1
      # 去除行末的换行符并按逗号分隔
      numbers = line.strip().split(',')
      
      # 检查是否有5个数字
      if len(numbers) != 5:
          break
      
      # 将字符串转换为浮点数
      num1 = float(numbers[0])
      num2 = float(numbers[1])
      num3 = float(numbers[2])
      num4 = float(numbers[3])
      num5 = float(numbers[4])

      global arm_client
      rospy.loginfo("正在导航机械臂....%f %f %f %f %f", num1, num2, num3, num4, num5)
      arm_client(num1, num2, num3, num4, num5)
      time.sleep(5)
      if n == 2:
        closeSuck()
      else:
        openSuck()

def pose_callback_test(msg):
  if msg.status.status == 3: 
    rospy.loginfo("已到达指定点...")
    initPos(getCurrentPos())
    moveDoBot2()

def main():
  # 初始化ros节点
  rospy.init_node('get_params')
  # 订阅位置信息
  global tf_listener, dobot_client, initialpose_pub,move_client,pose_subscriber, turtle_vel_pub, amcl_pose_pub, setHomeClient, arm_client,suck_client
  tf_listener = tf.TransformListener()  # 地图数据
  dobot_client = rospy.ServiceProxy('/DobotServer/GetPose', GetPose) # 机械臂位置
  turtle_vel_pub = rospy.Publisher('move_base_simple/goal', PoseStamped, queue_size=1) # 导航到指定点
  initialpose_pub = rospy.Publisher('/initialpose', PoseWithCovarianceStamped, queue_size=10) # 初始化设置
  amcl_pose_pub = rospy.Publisher('/amcl_pose', PoseWithCovarianceStamped, queue_size=10) # 初始化地图
  setHomeClient = rospy.ServiceProxy("/DobotServer/SetHOMECmd",SetHOMECmd) # 机械臂归零
  arm_client = rospy.ServiceProxy("/DobotServer/SetPTPCmd",SetPTPCmd) # 机械臂移动到指定位置
  suck_client = rospy.ServiceProxy("/DobotServer/SetEndEffectorSuctionCup",SetEndEffectorSuctionCup) # 吸盘
  move_client = rospy.Publisher('/cmd_vel', Twist, queue_size = 1) # 移动

  rospy.loginfo("初始化成功, 功能列表")
  rospy.loginfo("0: 初始化位置")
  rospy.loginfo("1: 获取当前小车的位置")
  rospy.loginfo("2: 获取当前机械臂的位置")
  rospy.loginfo("3: 导航到指定点") 
  rospy.loginfo("4: 机械臂归零")
  rospy.loginfo("5: 回家")
  rospy.loginfo("6: 前进0.2")
  rospy.loginfo("7: 机械臂导航")
  rospy.loginfo("8: 机械臂初始化")
  rospy.loginfo("9: 机械臂丢放测试")
  closeSuck()

  while True:
    choice = get_char()
    if choice == '0':
      initPos(InitPosVal(0, 0, 0, 0, 0, 0, 1))
    elif choice == '1':
      getCurrentPos()
    elif choice == '2':
      getDobotPos()
    elif choice == '3':
      dh(1)
    elif choice == '4':
      setHomeClient()
      time.sleep(25)
      arm_client(0, -5.27437448502, 207.521438599, 51.4118499756, 91.455909729)
      rospy.loginfo("机械臂归零结束!!")

    elif choice == '5':
      rospy.loginfo('正在回家......')
      turtle_vel_pub.publish(PoseStamped()) 
      time.sleep(1)
      rospy.Subscriber('/move_base/result', MoveBaseActionResult, pose_callback) 
      turtle_vel_pub.publish(MapPosVal(0, 0, 0, 0, 0, 0, 1))
    elif choice == '6':
      start_time = time.time()
      while time.time() - start_time <= 2 :
        move(0.3)
    elif choice == '7':
      moveDoBot()
    elif choice == '8':
      arm_client(0, -5.27437448502, 207.521438599, 51.4118499756, 91.455909729)
      time.sleep(5)
    elif choice == '9':
       moveDoBot2()
    else:
      break

    sys.stdout.flush()
  arm_client.close()
  setHomeClient.close()
  setHomeClient.close()
  dobot_client.close()

if __name__ == "__main__":
  main()


# 次位置  
# -0.00000000000, 0.00000000000, 0.138, 0.0, 0.0, 0.0, 1.0
# 0.49823367652, 0.01421743472, 0.138, 0.0, 0.0, -0.00395953597, 0.99999216101
# -1.59977255635, 0.92693193631, 0.138, 0.0, 0.0, -0.16561619251, 0.98619028426