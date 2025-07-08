import cv2
import mediapipe as mp
from pynput.keyboard import Controller
import time

# Initialize
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils
keyboard = Controller()

tip_ids = [4, 8, 12, 16, 20]
cap = cv2.VideoCapture(0)
cap.set(3, 320)  # Width (lower for speed)
cap.set(4, 240)  # Height

held_keys = set()

def update_keys(new_keys):
    global held_keys
    to_release = held_keys - new_keys
    to_press = new_keys - held_keys

    for key in to_release:
        keyboard.release(key)
    for key in to_press:
        keyboard.press(key)

    held_keys = new_keys

def fingers_status(lm_list):
    fingers = []

    # Thumb
    if lm_list[tip_ids[0]][0] > lm_list[tip_ids[0] - 1][0]:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other 4 fingers
    for id in range(1, 5):
        if lm_list[tip_ids[id]][1] < lm_list[tip_ids[id] - 2][1]:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers

while True:
    success, img = cap.read()
    if not success:
        break

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)
    new_keys = set()

    if result.multi_hand_landmarks:
        hand_landmarks = result.multi_hand_landmarks[0]
        lm_list = []

        for id, lm in enumerate(hand_landmarks.landmark):
            h, w, _ = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            lm_list.append((cx, cy))

        fingers = fingers_status(lm_list)
        total = fingers.count(1)

        # Map gestures to keys
        if total == 5:
            cv2.putText(img, "Turn Left ", (10, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            new_keys.add('a')

        elif total == 0:
            cv2.putText(img, "Turn Right ", (10, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
            new_keys.add('d')

        elif total == 2:
            cv2.putText(img, "Accelerate ", (10, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
            new_keys.add('w')

        elif fingers[1:] == [1, 1, 1, 1] and fingers[0] == 0:
            cv2.putText(img, "Brake ", (10, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            new_keys.add('s')

        else:
            cv2.putText(img, "Idle", (10, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 100, 100), 2)

        # Optional: draw hand (comment to reduce lag)
        mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    else:
        new_keys = set()

    update_keys(new_keys)
    cv2.imshow("Gesture Control - Racing Limits", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

update_keys(set())
cap.release()
cv2.destroyAllWindows()
