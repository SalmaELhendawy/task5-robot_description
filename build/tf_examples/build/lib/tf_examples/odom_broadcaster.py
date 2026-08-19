import math
import time
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
from tf2_ros import TransformBroadcaster


class OdomBroadcaster(Node):

    def __init__(self):
        super().__init__('odom_broadcaster')

        self.broadcaster = TransformBroadcaster(self)

        self.start_time = time.time()

        self.timer = self.create_timer(0.1, self.broadcast_transform)

    def broadcast_transform(self):
        t = time.time() - self.start_time

        transform = TransformStamped()

        transform.header.stamp = self.get_clock().now().to_msg()

        transform.header.frame_id = 'odom'
        transform.child_frame_id = 'base_footprint'

        transform.transform.translation.x = 0.2 * t
        transform.transform.translation.y = 0.3 * math.sin(0.5 * t)
        transform.transform.translation.z = 0.0

        yaw = 0.3 * math.sin(0.3 * t)

        transform.transform.rotation.x = 0.0
        transform.transform.rotation.y = 0.0
        transform.transform.rotation.z = math.sin(yaw / 2.0)
        transform.transform.rotation.w = math.cos(yaw / 2.0)

        self.broadcaster.sendTransform(transform)


def main():
    rclpy.init()

    node = OdomBroadcaster()

    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
