import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import threading


class Commander(Node):

	def __init__(self):
		super().__init__('commander')
		
		self.publisher = self.create_publisher(String,'/cmd',10)
		
		print("Command node started. Enter commands: ")
		
		self.input_thread = threading.Thread(target=self.input_loop)
		self.input_thread.daemon = True
		self.input_thread.start()
		
	def input_loop(self):
		while True:
			cmd = input()
			msg = String()
			msg.data = cmd
			
			self.publisher.publish(msg)
			
def main():
	rclpy.init()
	
	node = Commander()
	rclpy.spin(node)
	
	node.destroy_node()
	rclpy.shutdown()
	
if __name__ == '__main__':
	main()
