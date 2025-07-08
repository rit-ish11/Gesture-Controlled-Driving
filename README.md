#  Gesture-Controlled Driving Simulation using MediaPipe & OpenCV

Control a car in a racing game **using your hand gestures** instead of a keyboard or joystick!  
This project uses **MediaPipe** to track hand landmarks, detects gestures with **OpenCV**, and simulates keyboard actions using **Pynput** — enabling gesture-based gameplay in real time.

---

## 🎯 Features

- 🖐️ Real-time hand tracking via webcam
- 👆 Detects gestures like:
 4 fingers → Brake
2 fingers → Accelerate
0 fingers → Turn Right
5 fingers → Turn Left
- 🕹 Simulates keyboard keys (`W`, `A`, `S`, `D`) to control a driving game
- 🧠 Built using Python, MediaPipe, OpenCV, and Pynput

---

## 📹 Demo Video

🎬[Video Link](https://drive.google.com/file/d/your_video_id/view?usp=sharing](https://drive.google.com/file/d/14KWZ2fD7WKL1CuGMfe2Qgs1uOaA1x-FI/view?usp=sharing))



---

## 🧠 Technologies Used

| Module      | Purpose                     |
|-------------|-----------------------------|
| **Python**  | Core Programming Language    |
| **OpenCV**  | Video stream + image ops     |
| **MediaPipe** | Hand landmark detection     |
| **Pynput**  | Simulate keyboard inputs     |
| **VS Code** | IDE for development          |

---

## 💡 How It Works

1. **MediaPipe** detects 21 hand landmarks from webcam input
2. **Gesture logic** determines direction:
   - Left thumb extended → `A` (left)
   - Right thumb extended → `D` (right)
   - All fingers open → `W` (accelerate)
   - Fist (no fingers) → `S` (brake)
3. **Pynput** sends virtual key presses to game window

---

## 🧪 Setup & Installation

### 🔹 1. Clone the repository

```bash
git clone https://github.com/rit-ish11/gesture-driving-simulator.git
cd gesture-driving-simulator
