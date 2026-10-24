Project Title:
Bio-Inspired Human-Robot Interaction (HRI) System
Developed by : Mariam Elsaid
Field : Robotics Artificial Intelligence
Project Goal :
The goal of this project is to control a robot arm using human face movements, by
leverging computer vision and simulation technologies. This creates a "Hands-free"
system that make HRI easier and more natural and safe . Also on the other hand that
system is essential for future applications such as healthcare, industrial safety, and
human-computer interaction.
Tools used :
 Python 3.10+ : the primary programming language
 MediaPipe, OpenCV and ZMQ Remote API : for AI-based computer vision.
 CoppeliaSim (V-REP): for the robotics simulation environment using a Franka
Emika robot arm and communicating via the ZMQ Remote API.
How it works:
 Detection : the system uses a camera and artificial intelligence (MediaPipe) to
the track the face
 Processing : a Python based control loop that maps normalized X-coordinate of
the nose bridge to the joint space of the robot. Also it calculates the head
position and sends it to the simulator ( CoppeliaSim).
 Simulation : the robot in CoppeliaSim Follows the movement in real time.
Key Features :
 Real-Time Control: Fast response with no delay or any issues..
 Safety: The system stops immediately when pressing the ESC key for emergency
stops. .
 Efficiency: Works with a simple (webcam) or any camera in the device without
expensive and additional sensors.