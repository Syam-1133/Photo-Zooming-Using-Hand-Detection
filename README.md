## 📌 Photo Zooming Using Hand Detection 🎯  

This project allows users to **zoom in and out on images** and **navigate between photos** using **hand gestures**, specifically the **index finger and thumb** of the **right hand**. It uses **MediaPipe** for hand tracking and **PyAutoGUI** to control system zoom functions.  

---

## 🚀 Features  
✅ **Zoom In** → Spread index and thumb fingers apart  
✅ **Zoom Out** → Pinch index and thumb fingers together  
✅ **Next Photo** → Move hand left  
✅ **Previous Photo** → Move hand right  
✅ **Ultra-Smooth Performance** → Uses **exponential smoothing** for fast and fluid zooming  

---

## 📸 Demo  
[Add a GIF or screenshot of the working project]  

---

## 🛠️ Installation  

### 1️⃣ **Clone the Repository**  
```sh
git clone https://github.com/Syam-1133/Photo-Zooming-Using-Hand-Detection
```

### 2️⃣ **Install Dependencies**  
```sh
pip install opencv-python mediapipe numpy pyautogui
```

### 3️⃣ **Run the Script**  
```sh
python zoom.py
```

---

## 🏠 How It Works  

1. **MediaPipe** detects hand landmarks in real time.  
2. **Index and thumb finger distance** is measured dynamically.  
3. **Exponential smoothing** ensures smooth zooming.  
4. **PyAutoGUI sends system zoom commands** based on finger movement.  

🔹 **Pinch fingers (close distance) → Zoom Out**  
🔹 **Spread fingers (increase distance) → Zoom In**  
🔹 **Move hand left → Next Image**  
🔹 **Move hand right → Previous Image**  

---

## 🖥️ Tech Stack  

- **Python**  
- **OpenCV** (for video capture)  
- **MediaPipe** (for hand tracking)  
- **NumPy** (for distance calculation)  
- **PyAutoGUI** (for system control)  

---





