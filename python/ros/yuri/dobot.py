# _*_ coding: UTF-8 _*_
from dobot.srv  import *

import rospy
import sys
import tty
import termios
import time
from geometry_msgs.msg import Pose

class ArmController:
    def __init__(self):
        rospy.init_node('arm_controller')

        # setHomeClient = rospy.ServiceProxy("/DobotServer/SetHOMECmd",SetHOMECmd) # 机械臂归零
        # setHomeClient()
        # time.sleep(40)

        rospy.wait_for_service('/DobotServer/SetPTPCmd')
        self.pose_subscriber = rospy.ServiceProxy('/DobotServer/SetPTPCmd', SetPTPCmd)
        self.pose_subscriber(0, -5.27437448502, 207.521438599, 51.4118499756, 91.455909729)


        # 初始化机械臂位置信息
        self.a = 0
        self.b = -5.27437448502
        self.c = 207.521438599
        self.d = 51.4118499756
        self.e = 91.455909729

        

    def pose_callback(self, pose):
        # 更新当前位置信息
        self.current_pose = pose
        

    def control_arm(self):
        old_settings = termios.tcgetattr(sys.stdin)
        # 设置终端为无阻塞模式
        tty.setcbreak(sys.stdin.fileno())

        try:
            print("按下键盘 'ijklm' 来控制机械臂的方向")
            while not rospy.is_shutdown():
                # 读取键盘输入
                key = sys.stdin.read(1)

                # 根据按键调整机械臂位置
                if key == 'i':
                    self.b += 50
                elif key == 'k':
                    self.b -= 50
                elif key == 'j':
                    self.c += 30
                elif key == 'l':
                    self.c -= 10
                elif key == 'm':
                    self.d += 30
                elif key == 'n':
                    self.d -= 30
                elif key == 'g':
                    self.e += 10
                elif key == 'h':
                    self.e -= 10
                else:
                    break
                
                self.pose_subscriber(self.a, self.b, self.c, self.d, self.e)
                
                # # 显示当前位置信息
                print("当前位置：")
                print("b:", self.b) # 控制机械臂 左右转动角度 + 向右 - 向左
                print("c:", self.c) # 控制机械臂，伸展角度 + 向前伸展 - 向后
                print("d:", self.d) # 控制机械臂，上下角度 + 向上 - 向下
                print("e:", self.e)
                print()
                    

        finally:
            # 恢复终端默认模式
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

if __name__ == '__main__':
    
    controller = ArmController()
    controller.control_arm()
