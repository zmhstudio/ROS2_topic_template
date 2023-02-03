# a publisher demo for lcm together with ROS2

# import LCM headers
import lcm

# import ROS2 headers
import rclpy
from geometry_msgs.msg import Twist

import time

class lcm_cmd_vel(self):
	
def get_twist_msg(vel_from_ros):

	cmd_vel = Twist()
	pass
	return cmd_vel


def ros2_get_vel(args=None):

    	rclpy.init(args=args)

    	node = rclpy.create_node('vel_subscriber')

    	subscription = node.create_subscription(
        	Twist, 'cmd_vel', lambda msg: node.get_logger().info('I heard: "%s"' % msg), 10)
    	subscription  # prevent unused variable warning

    	rclpy.spin(node)
    	# Destroy the node explicitly
    	# (optional - otherwise it will be done automatically
    	# when the garbage collector destroys the node object)
    	node.destroy_node()
    	rclpy.shutdown()
	return msg
		
def main():
	
	lc = lcm.LCM("udpm://242.255.76.67:7667?ttl=255")

	msg = Twist()

	for i in range 5:
		
		lc.publish("cmd_vel", msg.encode())
		print("lcm publishing......")
		time.sleep(2)

if __name__ == "__main__":
	main()
