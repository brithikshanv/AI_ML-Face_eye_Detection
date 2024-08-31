Face Detection using OpenCV
This Python script uses OpenCV to perform real-time face detection via a webcam. It utilizes a Haar Cascade classifier to identify faces in video frames.

REQUIRMENTS:
•	Python 3.x
•	OpenCV (cv2)
You can install OpenCV using pip if you haven't already:
Copy code :  pip install opencv-python
WORKING:
1.	Load Haar Cascade Classifier: The script initializes a Haar Cascade classifier for detecting faces using the haarcascade_frontalface_default.xml file. Make sure this file is in the same directory as the script or provide the correct path.

2.	Initialize Camera: The script opens the default camera (camera index 0). If the camera fails to open, an error message is displayed, and the script exits.

3.	Capture Frames: In a loop, the script captures frames from the camera. Each frame is converted to grayscale for face detection.

4.	Face Detection: Faces are detected using the detectMultiScale method of the Haar Cascade classifier. Detected faces are highlighted with green rectangles.

5.	Display Frame: The processed frame is displayed in a window titled "Face Detection".

6.	Exit Condition: The loop continues until the 'ESC' key is pressed.

7.	Cleanup: The script releases the camera and closes all OpenCV windows upon exiting.

Usage
Ensure that haarcascade_frontalface_default.xml is in your working directory.
Run the script using Python:
Copy code  :  python face_detection.py
A window will appear showing the video feed from your webcam with detected faces highlighted. Press 'ESC' to exit.

TROUBLESHOOTING:
Camera Not Opening: Ensure no other application is using the camera and that the camera is correctly connected.
Haar Cascade File Not Found: Verify the path to haarcascade_frontalface_default.xml is correct.
