import rclpy 
from rclpy.node import Node
import cv2
import numpy as np

class VisionLock(Node):

	def __init__(self):
		super().__init__('vision_lock')
		
		# Open webcam
		self.cap = cv2.VideoCapture(0)
		
		# Timer runs every 0.03 secs (approx 30 FPS)
		self.timer = self.create_timer(0.03, self.process_frame)
		
	def process_frame(self):
		ret,frame = self.cap.read()
		
		if not ret:
			return
		
		height , width, _ = frame.shape
		
		# Convert to HSV
		hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
		
		# Blue color range
		lower_blue = np.array([100,150,50])
		upper_blue = np.array([140,255,255])
		
		# Creating a mask
		mask = cv2.inRange(hsv,lower_blue,upper_blue)
		
		# Finding contours for efficiency
		contours,_ = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
		
		state = "SEARCHING"
		output = frame.copy()

		if contours:
		    # Largest object
		    largest = max(contours, key=cv2.contourArea)

		    if cv2.contourArea(largest) > 500:
		        x, y, w, h = cv2.boundingRect(largest)
		        center_x = x + w // 2

		        # Draw rectangle
		        cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)

		        # LEFT THIRD
		        if center_x < width // 3:
		            state = "ALIGNING LEFT"

		            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		            output = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

		        # CENTER THIRD
		        elif center_x < 2 * width // 3:
		            state = "LOCKED ON"
		            output = frame.copy()

		        # RIGHT THIRD
		        else:
		            state = "ALIGNING RIGHT"

		            edges = cv2.Canny(frame, 100, 200)
		            output = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

		# If no object found
		if state == "SEARCHING":
		    output = cv2.bitwise_not(frame)

		# Print state
		print(state)

		# Show frame
		cv2.imshow("Vision Lock", output)

		# Press ESC to quit
		if cv2.waitKey(1) == 27:
		    self.cap.release()
		    cv2.destroyAllWindows()
		    rclpy.shutdown()


def main():
    rclpy.init()

    node = VisionLock()

    rclpy.spin(node)

    node.destroy_node()


if __name__ == '__main__':
    main()
