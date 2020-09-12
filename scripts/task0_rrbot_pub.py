#!/usr/bin/env python

import rospy 
from std_msgs.msg import Float64 #float as we saw the message type using rosmsg info

def rrbot_talker():
	pub1 = rospy.Publisher('/rrbot/joint1_position_controller/command', Float64, queue_size = 10)
	pub2 = rospy.Publisher('/rrbot/joint2_position_controller/command', Float64, queue_size = 10)
	rospy.init_node('rrbot_talker', anonymous = True)
	rate = rospy.Rate(5) # 5 Hz
	while not rospy.is_shutdown():
		joint_control = -1.5 #90 in radians
		pub1.publish(joint_control)
		pub2.publish(joint_control)
		rate.sleep

if __name__ == '__main__':
	try:
		rrbot_talker()
	except rospy.ROSInterruptException:
		pass
