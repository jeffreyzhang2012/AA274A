import rospy
from geometry_msgs.msg import Twist

def publisher():
    pub = rospy.Publisher('cmd_vel', Twist, queue_size = 10)
    rospy.init_node('talker',anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        move_cmd = Twist()
        move_cmd.linear.x = 0.0
        pub.publish(move_cmd)
        rate.sleep()


if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
