# publisher demo for topic:cmd_vel

import rclpy				# ros2 python interface
from geometry_msgs.msg import Twist	# ros2 cmd_vel template

import time 

# key phrases for establishing a publisher
def main(args = None):
	rclpy.init(args = args)					# initialize
	node = rclpy.create_node('cmd_vel_publisher')			# create a node 
	publisher = node.create_publisher(Twist, 'cmd_vel', 10)	# create a publisher 
	
	vel = Twist()		# define velocicity using the template
	
	vel.linear.x = 0.3	# the structure of class 'Twist':
	vel.linear.y = 0.3	# 	is {linear:{x,y,z}, angular:{x,y,z}}
	vel.linear.z = 0.3
	vel.linear.x = 0.3
	vel.linear.y = 0.3
	vel.linear.z = 0.3
	
	for i in range(5):
		publisher.publish(vel)			# publish the message 
		print("cmd_vel publishing")
		time.sleep(2)
	# rclpy.spin(node)
	
	
	node.destroy_node()				# clear the cache if finished publishing
	rclpy.shutdown()
		
if __name__ == "__main__":
	main()
	
