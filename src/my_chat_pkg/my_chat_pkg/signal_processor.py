import rclpy 
from rclpy.node import Node
from std_msgs.msg import Int32

class SignalProcessor(Node):

	def __init__(self):
		super().__init__('signal_processor')
		
		#for subscribing to /raw_signal
		self.subscription = self.create_subscription(
			Int32,
			'/raw_signal',
			self.process_signal,
			10
		)
		
		#for publishing to /processed_signal
		self.publisher = self.create_publisher(
			Int32,
			'/processed_signal',
			10
		)
		
	def process_signal(self,msg):
		
		#to get the incoming value
		input_value = msg.data
		
		#now we have to multiply by 5 for output
		output_value = input_value * 5
		
		#create a new msg to publish on the processed signal
		new_msg = Int32()
		new_msg.data= output_value
		
		#publishing the processed result
		self.publisher.publish(new_msg)
		
		#for checking whether its right or not (personal)
		print(f"Received: {input_value} -- Published: {output_value}")
		
def main():
	rclpy.init()
	
	node = SignalProcessor()
	rclpy.spin(node)
	
	node.destroy_node()
	rclpy.shutdown()
	
if __name__ == '__main__':
	main()
