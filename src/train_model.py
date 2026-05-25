import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import *

IMG_SIZE = 64
BATCH = 32

datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2
)

train = datagen.flow_from_directory(
    "dataset",
    target_size=(64,64),
    batch_size=BATCH,
    subset="training"
)

val = datagen.flow_from_directory(
    "dataset",
    target_size=(64,64),
    batch_size=BATCH,
    subset="validation"
)

model = Sequential([

    Conv2D(
        32,
        (3,3),
        activation='relu',
        input_shape=(64,64,3)
    ),

    MaxPooling2D(),

    Conv2D(
        64,
        (3,3),
        activation='relu'
    ),

    MaxPooling2D(),

    Flatten(),

    Dense(
        128,
        activation='relu'
    ),

    Dense(
        train.num_classes,
        activation='softmax'
    )
])

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(
    train,
    validation_data=val,
    epochs=10
)

model.save(
    "models/sign_model.h5"
)