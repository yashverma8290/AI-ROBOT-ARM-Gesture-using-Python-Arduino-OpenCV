import cv2
from cvzone.HandTrackingModule import HandDetector
import serial
import time

# Initialize serial communication (adjust COM port if needed)
arduino = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)  # wait for Arduino to reset

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1, detectionCon=0.7)

while True:
    success, img = cap.read()
    if not success:
        print("❌ Failed to grab frame")
        continue

    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        print(fingers)

        # Convert [1, 0, 1, 0, 1] to "$10101" and send
        data = "$" + ''.join(map(str, fingers))
        arduino.write(data.encode())  # Send over serial

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()
