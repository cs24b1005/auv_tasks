AUV TASK 1 :

Comm-link (ros2 pub/sub)

A ros2 node that acts as both a publisher and a subscriber on the /chat topic.

2 users can communicate in 2 different terminals using this.

commands used for running :
cd auv_ws
colcon build
source install/setup.bash

(obviously before this we need to activate ros2 on the terminal so we use source /opt/ros/humble/setup.bash for that)

use these commands in the 2 terminals for it to work:

ros2 run my_chat_pkg chat Invictus
ros2 run my_chat_pkg chat Hawcker


Issues I faced during this:
lot of syntax errors but i was able to rectify them soon
identifying where the multithreading is used in the script
setting up colcon for the compiling process took some time but eventually it started working
had to get used to the order in which the commands were supposed to be implemented (for ex: we need to activate the ro2 on the terminal before we move to the workspace and then we need to use colcon for the new package and then we need tto use the source install/setup.bash which loads my workspace into the current terminal which is why we have to do it for both the terminals)


