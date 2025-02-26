import cv2

cap = cv2.VideoCapture(0)  # 0 is the default camera index

if not cap.isOpened():
    print("Error: Could not open camera.")
else:
    print("Camera is accessible.")
    cap.release()
