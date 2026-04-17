import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class SignalOutput(Node):

	def __init__(self):
		super().__init__('signal_output')
		
		#now finally we're subscribing to the /processed_signal topic from this node
		self.subscription = self.create_subscription(
			Int32,
			'/processed_signal',
			self.final_output,
			10
		)
		
	def final_output(self,msg):
		#like the previous node we need to get the incoming value first
		input_value = msg.data
		
		#now we're adding 10 to obtain the final value 
		final_value = input_value + 10
		
		#printing the final value as the result
		print(f"Final Output: {final_value}")
		
def main():

	rclpy.init()
	
	node = SignalOutput()
	rclpy.spin(node)
	
	node.destroy_node()
	rclpy.shutdown()
	
if __name__ == '__main__':
	main()
