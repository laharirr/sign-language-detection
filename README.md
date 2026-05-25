# ✋ Sign Language Detection using Deep Learning

A real-time Sign Language Detection system built using **Python, TensorFlow, OpenCV, and MediaPipe**.  
The project detects hand gestures from webcam input and predicts sign language alphabets using a CNN-based deep learning model.

---

## 📌 Project Overview

This project aims to bridge communication gaps by recognizing sign language gestures in real time.

The system captures hand gestures using a webcam, processes the hand region using MediaPipe and OpenCV, and predicts the corresponding sign using a trained TensorFlow CNN model.

---

## 🚀 Features

- Real-time hand gesture detection
- MediaPipe hand landmark tracking
- CNN-based deep learning prediction
- Webcam live prediction
- Dataset collection support
- Model training and saving
- GitHub CI pipeline integration
- Modular project structure

---

## 🛠 Tech Stack

### Programming Language
- Python

### Computer Vision
- OpenCV
- MediaPipe

### Deep Learning
- TensorFlow
- Keras
- CNN (Convolutional Neural Network)

### Data Processing
- NumPy
- Matplotlib

### DevOps / Version Control
- Git
- GitHub
- GitHub Actions (CI Pipeline)

---

## 📂 Project Structure

```bash
Sign-Language-Detection
│
├── dataset/
│   ├── A/
│   ├── B/
│   └── C/
│
├── models/
│   └── sign_model.h5
│
├── src/
│   ├── mediapipe_collect.py
│   ├── train_model.py
│   ├── predict_live.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙ Installation

Clone repository:

```bash
git clone https://github.com/laharir/sign-language-detection.git
```

Move into project:

```bash
cd sign-language-detection
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 📷 Dataset Collection

Run:

```bash
python src/mediapipe_collect.py
```

Controls:

- **S** → Save image
- **Q** → Quit

Collect images for:

- A
- B
- C

Recommended:

- 200–300 images per label

---

## 🧠 Model Training

Train CNN model:

```bash
python src/train_model.py
```

After training:

Model saved as:

```bash
models/sign_model.h5
```

---

## 🔍 Live Prediction

Run:

```bash
python src/predict_live.py
```

The webcam opens and predicts hand signs in real time.

---

## 🔄 CI Pipeline

This project uses **GitHub Actions** for Continuous Integration.

Pipeline automatically:

- Checks out code
- Installs dependencies
- Validates Python files
- Reports build status

Workflow file:

```bash
.github/workflows/ci.yml
```

---

## 🧪 Future Improvements

- Full A–Z sign detection
- Sentence prediction
- Speech output
- Flask web deployment
- Docker containerization
- Cloud deployment
- MLOps pipeline

---

## 📈 Learning Outcomes

Through this project:

- Learned Computer Vision basics
- Understood MediaPipe hand tracking
- Built CNN models using TensorFlow
- Performed real-time prediction
- Used Git and GitHub
- Implemented CI pipeline concepts

---

## 👩‍💻 Author

Lahari R

GitHub: https://github.com/laharir
