#_*_coding:UTF-8_*_

import rospy
import tf
import time

if __name__ == '__main__':
  rospy.init_node('turtle_tf_listener') 

  listener = tf.TransformListener() 
  while not rospy.is_shutdown(): 
    time.sleep(1)
    try:
      (trans,rot) = listener.lookupTransform('map', 'base_link', rospy.Time(0)) 
    except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException): 
      continue
    x,y,z = trans[0], trans[1], trans[2]
    x_,y_,z_, w = rot[0], rot[1], rot[2], rot[3]
    print("pos -> {}, {}, {}, {}, {}, {}, {}".format(x,y,z, x_,y_, z_, w))
    # x: 坐标x轴 y 坐标y轴 z 坐标z轴 x_ ，y_ ,,,,, z_ w 转角