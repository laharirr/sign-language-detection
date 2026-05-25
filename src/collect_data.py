import cv2
import os

label = "D"
save_dir = f"dataset/{label}"

os.makedirs(save_dir, exist_ok=True)

cap = cv2.VideoCapture(0)

count = 0

while True:
    ret, frame = cap.read()

    cv2.imshow("Capture", frame)

    key = cv2.waitKey(1)

    if key == ord('s'):
        img_path = f"{save_dir}/{count}.jpg"
        cv2.imwrite(img_path, frame)
        print("Saved", count)
        count += 1

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()