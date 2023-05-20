import rospy
from std_srvs.srv import Empty
from std_srvs.srv import EmptyResponse

def hi_sur_callback(request):
    rospy.loginfo("Hi, My name is Hemnusornanon")
    return EmptyResponse()

def start_hi_sur_server():
    rospy.init_node('hi_sur_server')
    s = rospy.Service('/hi_sur', Empty, hi_sur_callback)
    rospy.loginfo("Ready to say hi!")
    rospy.spin()

if __name__ == '__main__':
    start_hi_sur_server()
