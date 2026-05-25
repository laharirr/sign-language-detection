import cv2
import numpy as np
from tensorflow.keras.models import load_model
import mediapipe as mp

model = load_model(
    "models/sign_model.h5"
)

labels = ['A','B','C']

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7
)

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    frame = cv2.flip(frame,1)

    rgb = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    result = hands.process(rgb)

    if result.multi_hand_landmarks:

        img = cv2.resize(
            frame,
            (64,64)
        )

        img = img/255.0

        img = np.expand_dims(
            img,
            axis=0
        )

        prediction = model.predict(
            img,
            verbose=0
        )

        label = labels[
            np.argmax(prediction)
        ]

        cv2.putText(
            frame,
            label,
            (50,50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255,0),
            2
        )

        for hand_landmarks in result.multi_hand_landmarks:

            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

    cv2.imshow(
        "Prediction",
        frame
    )

    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()