# Third Eye Smart Energy System

## Overview
Third Eye Smart Energy System is a vision-based solution that significantly reduces energy wastage using AI and computer vision technology. The system intelligently manages electrical devices based on real-time human presence detection, ensuring efficient and automated energy management without traditional sensors.

## How It Works
The system uses a camera to capture real-time video and applies the **YOLOv8 deep learning model** to detect human presence. Based on the detected position, the frame is divided into zones, and only the required electrical devices (lights, fans, etc.) are turned ON. Control signals are sent to an **ESP32 microcontroller**, which operates relay modules for precise device control.

## Key Features
- **Real-Time Vision-Based Detection**: Uses YOLOv8 for accurate human presence detection
- **Zone-Based Intelligence**: Divides captured frames into zones for targeted device control
- **Automated Device Management**: Intelligently turns ON/OFF lights, fans, and other appliances
- **IoT Integration**: Seamless ESP32 microcontroller communication via relay modules
- **Energy Efficiency**: Reduces energy wastage through intelligent automation
- **Sensor-Free Operation**: No traditional sensors required

## System Architecture
1. **Camera Module**: Captures real-time video feed
2. **YOLOv8 Model**: Detects and tracks human presence
3. **Zone Analysis**: Divides frame into controllable zones
4. **ESP32 Microcontroller**: Receives control signals and manages relays
5. **Relay Modules**: Control electrical devices (lights, fans, etc.)

## Requirements
- Python >= 3.8
- YOLOv8 dependencies
- ESP32 microcontroller
- Relay modules for device control
- Camera module/Webcam




## Contributing
Contributions are welcome! Please open an issue or submit a pull request to help improve the Third Eye Smart Energy System.



## Acknowledgements
- Thanks to Ultralytics for the YOLOv8 model
- Thanks to the open-source community for their invaluable resources
