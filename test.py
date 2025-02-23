import cv2

cap = cv2.VideoCapture(0)  # or 0, 1, 2, ...
if not cap.isOpened():
    print("Could not open camera index 0.")
    exit(1)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Could not read a frame from camera.")
        break
    cv2.imshow("Camera Test", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
