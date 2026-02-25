from ultralytics import YOLO
import cv2
import time
import serial

# ---------------- SERIAL SETUP ----------------
ser = serial.Serial("COM8", 115200, timeout=1)
time.sleep(2)

# ---------------- YOLO MODEL ----------------
model = YOLO("yolov8n.pt")
cap = cap = cv2.VideoCapture("http://10.82.201.78:8080/video")

cv2.namedWindow("Smart CCTV Energy System", cv2.WINDOW_NORMAL)

# ---------------- ZONES (Top=Lights, Bottom=Fans) ----------------
ZONES = {
    "Light_Left":   ((0, 0), (640, 360)),
    "Light_Right":  ((640, 0), (1280, 360)),
    "Fan_Left":     ((0, 360), (640, 720)),
    "Fan_Right":    ((640, 360), (1280, 720)),
}

ZONE_TIMEOUT = 3  # seconds before OFF

zone_last_seen = {zone: 0 for zone in ZONES}
zone_state = {zone: "OFF" for zone in ZONES}  # Track current state

# ---------------- FUNCTIONS ----------------

def draw_zones(frame):
    for name, ((x1, y1), (x2, y2)) in ZONES.items():
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 255), 2)
        cv2.putText(frame, name, (x1 + 10, y1 + 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

def get_zone(cx, cy):
    for name, ((x1, y1), (x2, y2)) in ZONES.items():
        if x1 <= cx <= x2 and y1 <= cy <= y2:
            return name
    return None

def send_command(zone, state):
    commands = {
        "Light_Left":  ("LL_ON", "LL_OFF"),
        "Light_Right": ("LR_ON", "LR_OFF"),
        "Fan_Left":    ("FL_ON", "FL_OFF"),
        "Fan_Right":   ("FR_ON", "FR_OFF"),
    }

    cmd = commands[zone][0] if state == "ON" else commands[zone][1]
    ser.write((cmd + "\n").encode())
    print(f"Sent: {cmd}")

# ---------------- MAIN LOOP ----------------

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (1280, 720))

    results = model(frame, classes=[0], conf=0.65)

    current_time = time.time()
    detected_zones = set()

    # --------- Detection Loop ----------
    for box in results[0].boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])

        width = x2 - x1
        height = y2 - y1
        area = width * height

        # False detection filtering
        if width < 80 or height < 150 or area < 20000:
            continue

        cx = (x1 + x2) // 2
        cy = (y1 + y2) // 2

        zone = get_zone(cx, cy)
        if zone:
            detected_zones.add(zone)
            zone_last_seen[zone] = current_time

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)

    draw_zones(frame)

    # --------- Smoothing + Serial Control ----------
    y_text = 30
    for zone in ZONES:
        if current_time - zone_last_seen[zone] < ZONE_TIMEOUT:
            new_state = "ON"
        else:
            new_state = "OFF"

        # Only send command if state changes
        if new_state != zone_state[zone]:
            send_command(zone, new_state)
            zone_state[zone] = new_state

        color = (0, 255, 0) if zone_state[zone] == "ON" else (0, 0, 255)

        cv2.putText(frame, f"{zone}: {zone_state[zone]}",
                    (10, y_text),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    color,
                    2)
        y_text += 30

    cv2.imshow("Smart CCTV Energy System", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
ser.close()
cv2.destroyAllWindows()