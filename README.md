# 🤖 AI-Powered Robotic Arm Using Python, Arduino & OpenCV

Control a 5-finger servo motor robotic hand using live webcam hand gesture detection via Python (OpenCV & Mediapipe). Your gestures control servo motors on Arduino in real-time.

---

## 🧠 Project Overview

- **Webcam captures hand** and detects finger positions using Python (OpenCV + Mediapipe).
- Python sends data like `$10101` via Serial to the Arduino.
- **Arduino controls 5 servo motors** (thumb to pinky) based on received gesture data.

---

## ✅ STEP 1: Hardware Setup

### 🔧 Components Needed

| Component                | Description                  |
|--------------------------|------------------------------|
| Arduino Uno/Nano         | Microcontroller              |
| USB Cable                | To connect Arduino to PC     |
| SG90 Servo Motors (x5)   | One for each finger          |
| Jumper Wires             | For connections              |
| Breadboard (optional)    | For organizing wiring        |
| External 5V Power Supply | (Recommended for servos)     |

---

### 🧩 Servo Motor Wiring

Each servo has:
- **Red wire → 5V**
- **Brown/Black wire → GND**
- **Orange/Yellow wire → Arduino PWM pin**

| Finger | Arduino Pin |
|--------|-------------|
| Thumb  | D7          |
| Index  | D9          |
| Middle | D11         |
| Ring   | D8          |
| Pinky  | D10         |

---

## ✅ STEP 2: Upload the Arduino Code

### 🧰 Tools Needed
- Download the **Arduino IDE**:  
  👉 https://www.arduino.cc/en/software

### 📄 Upload the following sketch from:
**`Arduino_code.ino`**

### 🖱️ Upload Instructions:
1. Open Arduino IDE.
2. Paste code from `Arduino_code.ino`.
3. Select:
   - **Tools > Board > Arduino Uno**
   - **Tools > Port > COM3** (or whichever your device shows)
4. Click **Upload (Right Arrow)**.
5. **Close Arduino IDE** after uploading to free the serial port.

---

## ✅ STEP 3: Python Environment Setup (PyCharm)

### 📦 Install Python Libraries

In your PyCharm terminal or command prompt:

```bash
pip install opencv-python mediapipe pyserial

## suggested Folder Structure
GestureRobotArmControl/
├── Arduino_code.ino
├── hand_to_arduino.py
├── demo.mp4
├── img1.png
└── README.md

✅ STEP 4: Python Code to Detect Hand & Send Data
Use the file:
  ->Arduino.py
This script:
  ->Uses your webcam to detect hand landmarks.
  ->Determines which fingers are up/down.
  ->Sends serial data like $10101 to the Arduino via pyserial.


✅ STEP 5: Run and Watch the Magic 🪄
🚀 Steps:
Connect Arduino to PC via USB.
Upload code using Arduino IDE (only once).
Close Arduino IDE.
Open PyCharm and run hand_to_arduino.py.
Show your hand in front of the webcam.
Watch the servos respond based on your finger gestures! 🎉

