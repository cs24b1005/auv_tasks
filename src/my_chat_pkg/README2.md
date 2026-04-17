TASK 2: Signal Processing Pipeline-

We need to implement a 3 node ROS2 pipeline.

Nodes:

1) signal_publisher: publishes integers to /raw_signal

2) signal_processor: subscribes to /raw_signal and multiplies each value by 5 and then publishes it to /processed_signal

3) signal_output: subscribes to /processed_signal and adds 10 to each value received and then prints the final output


Our Topics here are:

/raw_signal and /processed_signal


Steps for running:

ros2 run my_chat_pkg signal_pub

ros2 run my_chat_pkg signal_proc

ros2 run my_chat_pkg signal_out


Issues faced:
None since i was able to rectify everything after the first question's mistakes



