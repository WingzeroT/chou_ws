import rclpy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
import serial

esp32 = serial.Serial(port='/dev/ttyACM0', baudrate=2000000, timeout=.1)

def cmd_vel_callback(msg):
    # This function will be called whenever a message is received on the cmd_vel topic
    # msg is of type Twist
    linear_x = round(msg.linear.x, 2)
    angular_z = round(msg.angular.z, 2)
    data = '({}x{}z)'.format(linear_x,angular_z)
    esp32.write(bytes(data, 'utf-8'))
    #time.sleep(0.25)
    ser_data = esp32.readline()
    #print(ser_data)
    # Do something with the received Twist message
    #print("Linear X:", linear_x)
    #print("Angular Z:", angular_z)

def main():
    rclpy.init()
    node = rclpy.create_node('motor_node')
    # Subscribe to the cmd_vel topic with the cmd_vel_callback function as the callback
    subscriber = node.create_subscription(Twist, 'cmd_vel', cmd_vel_callback, 10)

    print("Starting...")

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
