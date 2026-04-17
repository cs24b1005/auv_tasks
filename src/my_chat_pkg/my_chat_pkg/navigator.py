import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Navigator(Node):
	def __init__(self):
		super().__init__('navigator')
		
		self.x = 0
		self.y = 0
		
		self.directions = ["North","East","South","West"]
		self.current_index = 0;
		
		self.subscription = self.create_subscription(String,'/cmd',self.process_command,10)
		
		self.publisher = self.create_publisher(String,'/bot_pose',10)
		
	def process_command(self,msg):
		cmd = msg.data.strip().lower()
		
		if cmd == "forward":
			if self.current_index == 0:
				self.y += 1
			elif self.current_index == 1:
				self.x += 1
			elif self.current_index == 2:
				self.y -= 1
			elif self.current_index == 3:
				self.x -= 1
				
		elif cmd == "backward":
			if self.current_index == 0:
				self.y -= 1
			elif self.current_index == 1:
				self.x -= 1
			elif self.current_index == 2:
				self.y += 1
			elif self.current_index == 3:
				self.x += 1
				
		elif cmd == "turn right":
			self.current_index = (self.current_index + 1) % 4
		elif cmd == "turn left":
			self.current_index = (self.current_index - 1) % 4
			
		msg = String()
		msg.data = f"Position: ({self.x}, {self.y}) and Facing: {self.directions[self.current_index]}"	
		self.publisher.publish(msg)
		
		print(f"Position: ({self.x}, {self.y}) and Facing: {self.directions[self.current_index]}")
		
		
def main():
	rclpy.init()
	
	node = Navigator()
	
	rclpy.spin(node)
	
	node.destroy_node()
	rclpy.shutdown()
	
if __name__ == '__main__':
	main()
