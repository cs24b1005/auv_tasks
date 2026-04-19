Task 4 - Operation Visual Lock (Vision + FSM)


We have to create a ROS2 node that uses the laptop webcam to detect a colored object and apply different visual filters based on the object's horizontal position on the screen.

Technologies Used:-

ROS2 Humble
Python
OpenCV
NumPy

Node Name:- vision_lock


The webcam feed is continuously captured using OpenCV. 
Each frame is converted from BGR format to HSV format for easier color detection.

A blue object is tracked using HSV masking.

The X-coordinate of the detected object's center is used to divide the screen into three zones:

- Left third
- Middle third
- Right third

If no object is detected, the system enters searching mode.

FSM States

1) ALIGNING LEFT
Condition:
Object center lies in left third of screen.

Filter Applied:
Grayscale

2) LOCKED ON
Condition:
Object center lies in middle third of screen.

Filter Applied:
Normal unfiltered webcam feed

3) ALIGNING RIGHT
Condition:
Object center lies in right third of screen.

Filter Applied:
Edge Detection using Canny

4) SEARCHING
Condition:
Object not detected.

Filter Applied:
Negative / Inverted colors

Output

The current state is displayed in terminal.


The processed video feed is shown in a separate OpenCV window.

How to Run

cd ~/auv_ws

colcon build

source install/setup.bash

ros2 run my_chat_pkg vision_lock
