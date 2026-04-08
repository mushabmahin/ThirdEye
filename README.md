# ThirdEye – Smart Energy Management System (Computer Vision + IoT)

## 🔍 Overview
An AI-powered system that automatically controls electrical devices (lights, fans) based on human presence using computer vision and IoT.

---

## Problem
Lights and electrical devices are often left ON in classrooms and offices even when no one is present, leading to unnecessary energy wastage.

---

## Approach
Built a real-time system that detects human presence and automates device control.

### Key Components:
- **Object Detection:** YOLOv8 Nano model to detect people in video streams  
- **Zone Mapping:** Maps detected person location to predefined zones  
- **Control Logic:** Determines which devices should be ON/OFF  
- **IoT Integration:** Sends commands to ESP32 to control relays  

### Workflow:
1. Capture live video from CCTV  
2. Detect humans using YOLOv8  
3. Map position to zones  
4. Send control signals to ESP32  
5. Automatically switch devices ON/OFF  

---

## Results
- Reduced unnecessary power usage by automating device control  
- Real-time detection and response using lightweight model  
- Stable operation using temporal smoothing (avoids flickering ON/OFF)  

---

## Tech Stack
- Python  
- YOLOv8 (Ultralytics)  
- OpenCV  
- ESP32  
- Serial Communication  

---

## Future Improvements
- Multi-person tracking  
- Smarter zone optimization  
- Deployment in large-scale environments  
