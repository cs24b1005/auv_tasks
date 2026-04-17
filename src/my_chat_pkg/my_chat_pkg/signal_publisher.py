import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class SignalPublisher(Node):

	def __init__(self):
		super().__init__('signal_publisher')
		#super used for calling constructor of parent class
		self.publisher = self.create_publisher(Int32,'/raw_signal',10)
		#starting point will be 2 ofc
		self.current_value = 2
		
		# we can use timer here for the 1 Hz requirement
		
		self.timer = self.create_timer(1.0,self.publish_signal)
		
	def publish_signal(self):
		#creating msg object of type int32
		msg = Int32()
		#assigning current value to the msg
		msg.data = self.current_value
		#publish the message to the /raw_signal topic
		self.publisher.publish(msg)
		#printing value to verify the thing thats being sent
		print(f"Published: {msg.data}")
		#update value for next cycle which is incrementing by 2
		self.current_value+=2
		
def main():
	rclpy.init()
	
	node = SignalPublisher()
	rclpy.spin(node)
	
	node.destroy_node()
	rclpy.shutdown()
	
if __name__ == '__main__':
	main()
		
		
