import cv2
import mediapipe as mp
import os

label = "C"

save_dir = f"dataset/{label}"
os.makedirs(save_dir, exist_ok=True)

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7
)

cap = cv2.VideoCapture(0)

count = len(os.listdir(save_dir))

while True:

    ret, frame = cap.read()
    frame = cv2.flip(frame,1)

    rgb = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    result = hands.process(rgb)

    if result.multi_hand_landmarks:

        for hand_landmarks in result.multi_hand_landmarks:

            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

    cv2.imshow(
        "Capture",
        frame
    )

    key = cv2.waitKey(1)

    if key == ord('s'):

        img_path = os.path.join(
            save_dir,
            f"{count}.jpg"
        )

        cv2.imwrite(
            img_path,
            frame
        )

        print(
            "Saved",
            img_path
        )

        count += 1

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()