import cv2
import mediapipe as mp
import numpy as np
import pyautogui
import time

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Start Video Capture
cap = cv2.VideoCapture(0)

def get_distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return np.linalg.norm(np.array(p1) - np.array(p2))

prev_distance = None
zoom_sensitivity = 0.03
min_zoom_distance = 30
last_zoom_time = time.time()


alpha = 0.3  # Controls smoothing strength (higher = faster response)
smoothed_distance = None

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Flip frame to mirror mode
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Hand Detection
    results = hands.process(image_rgb)

    if results.multi_hand_landmarks:
        for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
            handedness = results.multi_handedness[idx].classification[0].label

            if handedness == "Right":  # Process only the right hand
                # Get index finger and thumb coordinates
                index_x, index_y = int(hand_landmarks.landmark[8].x * w), int(hand_landmarks.landmark[8].y * h)
                thumb_x, thumb_y = int(hand_landmarks.landmark[4].x * w), int(hand_landmarks.landmark[4].y * h)

                # Draw landmarks
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Calculate finger distance
                distance = get_distance((index_x, index_y), (thumb_x, thumb_y))

                # Apply exponential smoothing for ultra-smooth transitions
                if smoothed_distance is None:
                    smoothed_distance = distance  # Initialize on first frame
                smoothed_distance = alpha * distance + (1 - alpha) * smoothed_distance

                # Prevent unnecessary rapid zooming
                if prev_distance is not None and time.time() - last_zoom_time > 0.05:
                    zoom_change = (smoothed_distance - prev_distance) * zoom_sensitivity

                    if smoothed_distance < min_zoom_distance:
                        print("Zoom Out (Fully Closed)")
                        pyautogui.hotkey('command', '-')  # Mac
                        # pyautogui.hotkey('ctrl', '-')  # Windows
                    elif zoom_change > 0.3:
                        print(f"Zoom In ({zoom_change:.2f})")
                        pyautogui.hotkey('command', '+')
                    elif zoom_change < -0.3:
                        print(f"Zoom Out ({zoom_change:.2f})")
                        pyautogui.hotkey('command', '-')

                    last_zoom_time = time.time()

                prev_distance = smoothed_distance
                break  # Process only the first detected right hand

    # Show the camera feed
    cv2.imshow("Hand Tracking", frame)

    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
