# -*- coding: utf-8 -*-


import rospy
import time
import rospy
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import PoseWithCovarianceStamped
import os

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

def GetPackage():
    # 获取包的位置
    package_location = os.path.dirname(PoseStamped.__file__)
    print("Package location:", package_location)

if __name__ == '__main__':
    GetPackage()