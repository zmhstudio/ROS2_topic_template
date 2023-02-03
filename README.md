This is a simple template of sending or receiving ROS2 messages through LCM.

The most common ROS2 message in robotics is 'cmd_vel'.

The basic format of 'cmd_vel' is: 
	vel = Twist()		# define velocicity using the template
	
	vel.linear.x = 0.3	# the structure of class 'Twist':
	vel.linear.y = 0.3	# 	is {linear:{x,y,z}, angular:{x,y,z}}
	vel.linear.z = 0.3
	vel.angular.x = 0.3
	vel.angular.y = 0.3
	vel.angular.z = 0.3

Alter the linear and angular value to match your need if use. 
