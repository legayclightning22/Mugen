# object_detection.py
# Author: Hemendra
# Refactored to provide run_vision_system() function

import cv2
import random

def mock_object_detection(frame):
    objects = ['bottle', 'cup', 'book', 'phone', 'keys']
    detected_objects = []

    num_objects = random.randint(0, 2)
    for _ in range(num_objects):
        obj = random.choice(objects)
        x, y = random.randint(50, 300), random.randint(50, 300)
        detected_objects.append((obj, (x, y)))

    return detected_objects

def run_vision_system():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Cannot open camera")
        return

    print("Starting mock object detection. Press 'q' to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        detections = mock_object_detection(frame)
        for obj_name, (x, y) in detections:
            cv2.putText(frame, obj_name, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.circle(frame, (x, y), 10, (0, 255, 0), -1)

        cv2.imshow('Hemendra\'s Robot Vision', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Quitting object detection.")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_vision_system()
