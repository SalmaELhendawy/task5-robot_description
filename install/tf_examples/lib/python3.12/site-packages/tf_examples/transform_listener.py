import rclpy

from rclpy.node import Node

from tf2_ros import Buffer
from tf2_ros import TransformListener


class SimpleTransformListener(Node):

    def __init__(self):

        super().__init__('transform_listener')

        self.tf_buffer = Buffer()

        self.tf_listener = TransformListener(
            self.tf_buffer,
            self
        )

        self.timer = self.create_timer(
            1.0,
            self.lookup_transform
        )

    def lookup_transform(self):

        try:

            transform = self.tf_buffer.lookup_transform(
                'odom',
                'base_footprint',
                rclpy.time.Time()
            )

            x = transform.transform.translation.x
            y = transform.transform.translation.y

            self.get_logger().info(
                f'x={x:.2f}, y={y:.2f}'
            )

        except Exception:
            pass


def main():

    rclpy.init()

    node = SimpleTransformListener()

    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
