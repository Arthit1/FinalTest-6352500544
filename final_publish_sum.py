import rospy
from std_msgs.msg import Int64

def publish_sum_std_id():
    rospy.init_node('sum_std_id_publisher', anonymous=True)
    pub = rospy.Publisher('/sum_std_id', Int64, queue_size=10)
    rate = rospy.Rate(10)  # 10 Hz

    sum_std_id = 6352500544

    while not rospy.is_shutdown():
        pub.publish(sum_std_id)
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_sum_std_id()
    except rospy.ROSInterruptException:
        pass
