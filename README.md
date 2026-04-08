# ThirdEye – Real-Time Object Detection System

## Problem
Visually impaired individuals and distracted pedestrians often lack real-time awareness of their surroundings, increasing the risk of accidents. Existing solutions are either expensive, slow, or not optimized for real-time detection on lightweight systems.

## Approach
Developed a real-time object detection system using YOLOv8 to identify and classify objects from live video input.

The system processes frames from a camera feed and detects objects with bounding boxes and labels in real time. Optimized for speed and efficiency to work on standard hardware.

Key steps:
- Integrated YOLOv8 pre-trained model for object detection
- Processed live video stream using OpenCV
- Implemented frame-by-frame detection and visualization
- Focused on balancing accuracy and latency

## Results
- Achieved real-time object detection with minimal latency  
- Successfully detected multiple objects simultaneously  
- Demonstrated reliable performance on standard hardware  
- Improved situational awareness through visual feedback  

## Tech Stack
- Python  
- OpenCV  
- YOLOv8  
- NumPy  

## Demo
Run the following command to start the detection system:

```bash
python pd.py
