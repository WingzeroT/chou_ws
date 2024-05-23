import rclpy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
import serial

esp32 = serial.Serial(port='/dev/ttyACM1', baudrate=2000000, timeout=.1)
cmd_vel_data = None
joy_data = None

def cmd_vel_callback(msg):
    global cmd_vel_data
    linear_x = round(msg.linear.x, 2)
    angular_z = round(msg.angular.z, 2)
    cmd_vel_data = '({}x{}z'.format(linear_x, angular_z)
    if joy_data is not None:
        send_data()

def joy_callback(msg):
    global joy_data
    dpad_vertical = msg.axes[7]
    dpad_horizontal = msg.axes[6]
    right_vertical_axis_value = round(msg.axes[3], 2)
    right_horizontal_axis_value = round(msg.axes[2], 2)
    left_bumper = msg.buttons[6]
    joy_data = '{}c{}n{}v{}h{}l)'.format(right_vertical_axis_value, right_horizontal_axis_value, dpad_vertical, dpad_horizontal, left_bumper)
    if cmd_vel_data is not None:
        send_data()

def send_data():
    global cmd_vel_data, joy_data
    combined_data = cmd_vel_data + joy_data
    esp32.write(bytes(combined_data, 'utf-8'))
    cmd_vel_data = None
    joy_data = None

def main():
    rclpy.init()
    node = rclpy.create_node('subscriber_node')
    
    subscriber_cmd_vel = node.create_subscription(Twist, 'cmd_vel', cmd_vel_callback, 10)
    subscriber_joy = node.create_subscription(Joy, 'joy', joy_callback, 10)

    print("Starting...")

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
