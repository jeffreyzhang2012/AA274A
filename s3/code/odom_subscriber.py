import rospy
from nav_msgs.msg import Odometry

def callback(data):
    rospy.loginfo(data)


def subscriber():
    rospy.init_node('listenner', anonymous=True)
    rospy.Subscriber("odom", Odometry, callback)
    rospy.spin()


if __name__ == '__main__':
    subscriber()
