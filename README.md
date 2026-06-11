# 🔥 Forest Fire and Smoke Detection System using Computer Vision & Machine Learning

## 📌 Overview

Forest fires are one of the major environmental threats causing damage to forests, wildlife, and human life. Early detection of smoke and fire can help reduce disaster impact.

This project builds an AI-powered **Forest Fire and Smoke Detection System** that uses aerial/forest imagery to detect early signs of smoke and fire.

The system follows a safety-first approach:

- ✅ False alarms are acceptable
- ❌ Missing an actual forest fire is not acceptable

Therefore, the model focuses on improving **Recall** rather than only maximizing accuracy.

---

# 🚀 Features

- Upload forest/drone images
- Automatic image feature extraction using Computer Vision
- Fire and smoke pattern analysis
- Early fire risk prediction
- Fire probability score generation
- Streamlit based interactive dashboard
- Recall-focused decision threshold

---

# 🧠 Problem Statement

Traditional fire detection systems face challenges such as:

- Confusing smoke with clouds or fog
- Missing early-stage fires
- Handling rare fire events
- Class imbalance problems
- Over-dependence on accuracy

This project focuses on detecting weak visual fire signals from aerial images.

---

# 🛰️ Computer Vision Features

The following features are extracted from images:

| Feature | Purpose |
|--------|---------|
| Mean Red | Measures red color intensity |
| Mean Green | Measures vegetation/brightness |
| Mean Blue | Measures blue channel intensity |
| Red-Blue Ratio | Detects flame color dominance |
| Smoke Whiteness | Identifies smoke-like regions |
| Haze Index | Detects smoky environment |
| Hot Pixel Fraction | Finds fire-colored pixels |
| Edge Density | Detects texture changes |
| Intensity STD | Brightness variation |
| Local Contrast | Measures image contrast |

---

# 🏗️ System Architecture

```
Forest / Drone Image

        ↓

Computer Vision Processing
(OpenCV)

        ↓

Feature Extraction

        ↓

Machine Learning Model

        ↓

Fire Probability Prediction

        ↓

Warning Generation

🔥 High Fire Alert
⚠️ Possible Smoke
🌲 Safe Forest
```

---

# 🤖 Machine Learning Approach


## Logistic Regression Baseline

Implemented to understand:

- Weak visual signals
- Feature importance
- Class imbalance behavior


## Gradient Boosting Classifier

Used as the final model because:

- Handles nonlinear relationships
- Learns difficult fire patterns
- Performs well on structured CV features
- Improves rare event detection

---

# 📊 Evaluation Strategy

Accuracy alone is not reliable for forest fire detection.

Example:

A model predicting "No Fire" most of the time may achieve high accuracy but fail during real disasters.

Important metrics:

- Recall
- Precision
- F1 Score
- Precision-Recall Curve

Priority:

```
Recall > Accuracy
```

because detecting every possible fire is more important than reducing false alarms.

---

# 🛠️ Technology Stack

- Python
- OpenCV
- NumPy
- Pandas
- Scikit-Learn
- Gradient Boosting Classifier
- Logistic Regression
- Streamlit

---

# 📂 Project Structure

```
Forest-Fire-Detection/

│
├── app.py
│
├── model.ipynb
│
├── fire_model.pkl
│
├── scaler.pkl
│
├── Forest Fire Smoke Dataset.csv
│
├── requirements.txt
│
└── README.md

```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Kavya2605/Forest-Fire-and-Smoke-Detection.git
```

Move into project folder:

```bash
cd Forest-Fire-and-Smoke-Detection
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🏋️ Model Training

Run:

```bash
python model.ipynb
```

The training process generates:

```
fire_model.pkl

scaler.pkl
```

---

# 🌐 Run Streamlit Application

Start the application:

```bash
streamlit run app.py
```

---

# 📷 Application Workflow

1. Upload forest/aerial image

2. Image preprocessing using OpenCV

3. Extract visual features

4. Normalize features

5. Predict using trained model

6. Generate alert level


Output examples:

🔥 HIGH FIRE ALERT

⚠️ Possible Smoke / Early Fire Detected

🌲 No Fire Detected

---

# 🔥 Fire Detection Logic

The system analyzes:

### Flame Indicators

- High red intensity
- Red-blue dominance
- Hot pixel regions


### Smoke Indicators

- White/gray regions
- Haze patterns
- Low contrast areas


Combined signals improve early detection.

---

# 🌎 Real World Challenges Considered

- Smoke vs clouds confusion
- Different lighting conditions
- Small fire regions
- Hidden flames behind smoke
- Rare fire events
- Class imbalance

---

# 🚀 Future Improvements

- CNN based deep learning model
- Satellite image analysis
- Drone video monitoring
- Temporal fire tracking
- Thermal image processing
- Multi-sensor fusion

---

# 📌 Key Learnings

- Computer Vision feature engineering
- Image preprocessing
- Handling imbalanced datasets
- Recall optimization
- Real-world AI safety system design
- ML model deployment

---

# 👩‍💻 Author

**Kavya Ponduru**

AI/ML Engineer  
Computer Vision | Machine Learning | Deep Learning

---

⭐ If you like this project, give it a star!