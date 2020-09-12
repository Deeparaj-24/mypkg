#!/usr/bin/env python

import rospy 
from std_msgs.msg import String

def talker():
	pub = rospy.Publisher('chatter', String, queue_size = 10)#Topic name, msg type
	rospy.init_node('talker', anonymous = True)# Name of the node, Anon=True to avoid clashing of topic names when there are many nodes involved
	rate = rospy.Rate(5) #5Hz-frequency
	

	while not rospy.is_shutdown():
		msg_to_pub = "Hey There!! %s" % rospy.get_time()
		pub.publish(msg_to_pub)
		rate.sleep
if __name__ == '__main__': 
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
