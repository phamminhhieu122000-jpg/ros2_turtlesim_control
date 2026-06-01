#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import sys
import termios
import tty

msg = """
-----------------------------------------
Điều khiển chú rùa bằng phím WASD:
-----------------------------------------
        W : Tiến lên
A : Xoay trái       D : Xoay phải
        S : Lùi lại

Bấm SPACE (Khoảng trắng) để Dừng rùa hoàn toàn
Bấm CTRL+C để Thoát chương trình
-----------------------------------------
"""

class WASDControlNode(Node):
    def __init__(self):
        super().__init__('wasd_control_node')
        # Tên biến chuẩn chỉnh, không thừa chữ w, không thừa chữ s
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.get_logger().info("Node WASD Control đã khởi chạy thành công!")

    def get_key(self):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

    def run(self):
        print(msg)
        twist = Twist()
        
        while True:
            key = self.get_key()
            
            if key == 'w' or key == 'W':
                twist.linear.x = 2.0
                twist.angular.z = 0.0
            elif key == 's' or key == 'S':
                twist.linear.x = -2.0
                twist.angular.z = 0.0
            elif key == 'a' or key == 'A':
                twist.linear.x = 0.0
                twist.angular.z = 2.0
            elif key == 'd' or key == 'D':
                twist.linear.x = 0.0
                twist.angular.z = -2.0
            elif key == ' ':
                twist.linear.x = 0.0
                twist.angular.z = 0.0
            elif key == '\x03':
                break
            else:
                continue

            # Gọi đúng tên biến đã khai báo ở trên
            self.publisher_.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = WASDControlNode()
    try:
        node.run()
    except KeyboardInterrupt:
        pass
    finally:
        stop_twist = Twist()
        node.publisher_.publish(stop_twist)
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()