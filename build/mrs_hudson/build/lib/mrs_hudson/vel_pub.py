import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


def main(args=None):
    rclpy.init(args=args)
    pub = Node("cmd_vel_publisher")
    publisher_ = pub.create_publisher(Twist, 'cmd_vel', 10)
    msg = Twist()
    msg.linear.x = 1.0
    publisher_.publish(msg)

if __name__ == '__main__':
    main()
