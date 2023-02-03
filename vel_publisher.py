import rospy
import time 
from geometry_msgs.msg import Twist

def main():
	vel_pub = rospy.Publisher('cmd_vel', Twist, 10)
	vel_node = rospy.init_node('cmd_vel_publisher', anonymous = True)

	vel = Twist()
	vel.linear.x = 0.3	# the structure of class 'Twist':
	vel.linear.y = 0.3	# 	is {linear:{x,y,z}, angular:{x,y,z}}
	vel.linear.z = 0.3
	vel.linear.x = 0.3
	vel.linear.y = 0.3
	vel.linear.z = 0.3

	for i in range(5):
		time.sleep(1)
		vel_pub.publish(vel)
		timr.sleep(1)
		print("publishing...")

	

if __name__ == "__main__":
	main()
