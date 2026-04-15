import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import threading
import sys

class ChatNode(Node):

	def __init__(self,username):
		super().__init__('chat_node')
		
		self.username = username
		
		self.publisher = self.create_publisher(String, '/chat' , 10)
		
		self.subscription = self.create_subscription(
			String,
			'/chat',
			self.chat_callback,
			10
		)
		
		print(f"[{self.username}] Chat node started")
		
		self.input_thread = threading.Thread(target=self.input_loop)
		self.input_thread.daemon = True
		self.input_thread.start()
		
	def chat_callback(self,msg):
		print(msg.data)
	def input_loop(self):
		while True:
			text = input()
			message = String()
			message.data = f"[{self.username}]: {text}"
			self.publisher.publish(message)
			
def main():
	rclpy.init()
	
	if len(sys.argv) < 2:
		print("Usage: ros2 run my_chat_pkg chat <username>")
		return
		
	username = sys.argv[1]
	node = ChatNode(username)
	
	rclpy.spin(node)
	node.destroy_node()
	rclpy.shutdown()
	
if __name__ == '__main__':
	main()
