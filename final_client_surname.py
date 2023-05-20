import rospy
from std_srvs.srv import Empty

def call_hi_sur_service():
    rospy.init_node('hi_sur_client')
    rospy.wait_for_service('/hi_sur')
    try:
        hi_sur = rospy.ServiceProxy('/hi_sur', Empty)
        response = hi_sur()
        rospy.loginfo("Received response: %s", response)
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s", e)

if __name__ == '__main__':
    call_hi_sur_service()
