TASK 3: Dead Reckoning System using FSM and ROS2

We need to implement a commander and a navigator ROS2 system using state machine logic.

Nodes:

1) Commander: accepts user commands and publishes it to /cmd topic

2) Navigator: subscribes to the /cmd topic and updates the x position,y position and the facing direction

It then publishes it a another topic called /bot_pose

Commands:
forward

backward

turn left

turn right


Starting State: 
Position - (0,0) and facing- North

Steps to run:

ros2 run my_chat_pkg commander
ros2 run my_chat_pkg navigator
