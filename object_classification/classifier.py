import cv2

# Our Image
# video = cv2.VideoCapture("video1.avi")
video = cv2.VideoCapture(r"D:\Object_Test\video\REF_CAM_{2021.06.22_at_07.14.47_radar-mi_191.rrec}_DOC_CAM_Front.mp4")

# Pre-trained Car classifier
cars_classifier_file = r"D:\Object_Test\model\cars.xml"
pedestrians_classifier_file = r"D:\Object_Test\model\haarcascade_fullbody.xml"

# Create a Car Classifier
car_tracker = cv2.CascadeClassifier(cars_classifier_file)
pedestrian_tracker = cv2.CascadeClassifier(pedestrians_classifier_file)

while True:
    # Read the current frame
    (read_successful, frame) = video.read()

    if read_successful:
        # Convert to grayscale
        grayscaled_frames = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    # Detect the car
    cars = car_tracker.detectMultiScale(grayscaled_frames)
    pedestrians = pedestrian_tracker.detectMultiScale(grayscaled_frames)

    # Draw the rectange around the cars
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)  # BGR,thickness-2

    # Draw the rectange around the cars
    for (x, y, w, h) in pedestrians:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # BGR,thickness-2

    # Display the image with the car spotted
    cv2.imshow("Nidhi's Cars and Pedestrians Detector", frame)

    # Don't AutoClose (wait here for a key press)
    cv2.waitKey(1)

    print("Yuhooo!! Coding Completed :)")

