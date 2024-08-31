import cv2

# Load the cascade classifier
face_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

# Initialize camera
camera = cv2.VideoCapture(0)

# Check if camera opened successfully
if not camera.isOpened():
    print("Error: Unable to open camera.")
    exit()


# Loop to capture frames from the camera
while True:
    # Capture frame-by-frame
    ret, frame = camera.read()

    # Check if frame is read correctly
    if not ret:
        print("Error: Unable to read frame.")
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Face Detection', frame)

    # Break the loop if 'ESC' key is pressed
    if cv2.waitKey(1) == 27:
        break

# Release the camera and close all windows
camera.release()
cv2.destroyAllWindows()