# 🔥 Forest Fire and Smoke Detection System using Computer Vision & Machine Learning

## 📌 Overview

Forest fires cause severe environmental damage, and early detection is critical to prevent large-scale disasters.  
This project develops an AI-powered **Forest Fire and Smoke Detection  System** that analyzes aerial/drone imagery to identify early signs of **fire and smoke**.

The system is designed with a safety-first approach:

- ✅ False alarms are acceptable
- ❌ Missing an actual fire is highly undesirable

Instead of optimizing only accuracy, the model focuses on **high recall** to detect potential fire events as early as possible.


---

## 🚀 Features

- Upload forest/aerial images through a Streamlit web application
- Automatic Computer Vision feature extraction
- Smoke and fire pattern analysis
- Fire probability prediction
- Early warning alert system
- Optimized for rare fire event detection


---

## 🧠 Problem Statement

Traditional fire detection systems often fail because they:

- Treat smoke and fire patterns incorrectly
- Ignore class imbalance
- Depend only on accuracy
- Miss early-stage fire indicators

This project focuses on identifying weak but important visual signals from aerial images.


---

## 🛰️ Computer Vision Features Extracted

The following image-based features are extracted using OpenCV:

| Feature | Description |
|-------|-------------|
| Mean Red | Average red channel intensity |
| Mean Green | Average green channel intensity |
| Mean Blue | Average blue channel intensity |
| Red-Blue Ratio | Detects flame color dominance |
| Smoke Whiteness | Measures smoke-like regions |
| Haze Index | Detects smoky atmospheric effect |
| Hot Pixel Fraction | Identifies flame-colored pixels |
| Edge Density | Texture variation detection |
| Intensity STD | Brightness variation |
| Local Contrast | Image contrast information |


---

## 🏗️ System Architecture


Forest Image / Drone Image

            ↓

Computer Vision Processing (OpenCV)

            ↓

Feature Extraction

            ↓

Machine Learning Model

            ↓

Fire Risk Prediction

            ↓

Streamlit Alert Dashboard


---

## 🤖 Machine Learning Approach


### 1. Logistic Regression Baseline

Used for:

- Understanding weak visual signals
- Analyzing feature contribution
- Studying class imbalance effects


### 2. Gradient Boosting Classifier

Final model because it:

- Learns complex nonlinear patterns
- Focuses on difficult samples
- Handles rare fire cases better
- Improves recall performance


---

## 📊 Model Evaluation

Accuracy alone is not sufficient for this problem.

Important metrics:

- Recall
- Precision
- F1 Score
- Precision-Recall Curve


Priority:

Recall > Accuracy

because missing a real forest fire is more dangerous than a false alert.


---

## 🛠️ Tech Stack

- Python
- OpenCV
- NumPy
- Pandas
- Scikit-Learn
- Gradient Boosting
- Logistic Regression
- Streamlit


---

## 📂 Project Structure

Forest-Fire-Detection/

│

├── app.py

├── model.ipynb

├── fire_model.pkl

├── scaler.pkl

├── Forest Fire Smoke Dataset.csv

├── requirements.txt

└── README.md



---

## ⚙️ Installation


Clone repository:


```bash
git clone https://github.com/Kavya2605/Forest-Fire-Smoke-Detection.git

cd Forest-Fire-Smoke-Detection

Install dependencies:

---
pip install -r requirements.txt
```bash

🏋️ Train Model

Run:
---
python model.ipynb

```bash

This creates:
---
fire_model.pkl
scaler.pkl

```bash

🌐 Run Streamlit Application
---
streamlit run app.py

```bash

Upload a forest image and the system predicts:

🔥 High Fire Alert

⚠️ Possible Smoke / Early Fire

🌲 Safe Forest

📷 Application Workflow
User uploads aerial image
OpenCV extracts visual features
Features are normalized
ML model predicts probability
Warning level generated

🌎 Real World Challenges Considered
Smoke vs cloud confusion
Changing sunlight conditions
Fire hidden by dense smoke
Class imbalance
Rare event detection

Future improvements:
CNN-based image classification
Satellite imagery integration
Temporal fire tracking
Multi-sensor fusion
Thermal camera support

📌 Key Learning Outcomes
Computer Vision feature engineering
Handling imbalanced datasets
Recall-focused ML design
Real-world AI safety considerations
ML model deployment

👩‍💻 Author

Kavya Ponduru

AI/ML Engineer | Computer Vision | Deep Learning
