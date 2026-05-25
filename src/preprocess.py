import cv2
import os

IMG_SIZE = 64

for label in os.listdir("dataset"):
    path = os.path.join("dataset", label)

    for img_name in os.listdir(path):

        img_path = os.path.join(path, img_name)

        img = cv2.imread(img_path)

        img = cv2.resize(
            img,
            (IMG_SIZE, IMG_SIZE)
        )

        cv2.imwrite(img_path, img)

print("Done")