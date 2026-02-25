from ultralytics import YOLO
import cv2

# Load YOLO model
model = YOLO("yolov8n.pt")

# Start camera
cap = cv2.VideoCapture(0)

cv2.namedWindow("Smart CCTV Energy System", cv2.WINDOW_NORMAL)

# Define zones
ZONES = {
    "Light_Front_Left":  ((0, 480), (640, 720)),
    "Light_Front_Right": ((640, 480), (1280, 720)),

    "Fan_Middle_Left":   ((0, 240), (640, 480)),
    "Fan_Middle_Right":  ((640, 240), (1280, 480)),

    "Fan_Back_Left":     ((0, 0), (640, 240)),
    "Fan_Back_Right":    ((640, 0), (1280, 240)),
}

def draw_zones(frame, zones):
    for name, ((x1, y1), (x2, y2)) in zones.items():
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 255), 2)
        cv2.putText(frame, name, (x1 + 10, y1 + 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

def get_zone(cx, cy, zones):
    for name, ((x1, y1), (x2, y2)) in zones.items():
        if x1 <= cx <= x2 and y1 <= cy <= y2:
            return name
    return None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (1280, 720))

    # 🔥 Increase confidence threshold
    results = model(frame, classes=[0], conf=0.65)

    active_zones = set()

    for box in results[0].boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = float(box.conf[0])

        width = x2 - x1
        height = y2 - y1
        area = width * height

        # 🔥 FILTER CONDITIONS (IMPORTANT)
        if width < 80:
            continue
        if height < 150:
            continue
        if area < 20000:
            continue

        cx = (x1 + x2) // 2
        cy = (y1 + y2) // 2

        zone = get_zone(cx, cy, ZONES)
        if zone:
            active_zones.add(zone)

        # Draw detection
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)

    # Draw zones
    draw_zones(frame, ZONES)

    # Display ON/OFF status
    y_text = 30
    for zone in ZONES:
        status = "ON" if zone in active_zones else "OFF"
        color = (0, 255, 0) if status == "ON" else (0, 0, 255)
        cv2.putText(frame, f"{zone}: {status}", (10, y_text),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
        y_text += 30

    cv2.imshow("Smart CCTV Energy System", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()