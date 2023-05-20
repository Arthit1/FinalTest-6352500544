import rospy
from std_msgs.msg import Int64

def sum_std_id_callback(data):
    rospy.loginfo("Received sum_std_id: %d", data.data)

def subscribe_sum_std_id():
    rospy.init_node('sum_std_id_subscriber', anonymous=True)
    rospy.Subscriber('/sum_std_id', Int64, sum_std_id_callback)

    rospy.spin()

if __name__ == '__main__':
    try:
        subscribe_sum_std_id()
    except rospy.ROSInterruptException:
        pass
