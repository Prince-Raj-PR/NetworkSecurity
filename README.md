# 🔐 Network Security ML Pipeline

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![ML](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)
![Tracking](https://img.shields.io/badge/Experiment%20Tracking-MLflow-blue)
![Database](https://img.shields.io/badge/Database-MongoDB-green)
![Status](https://img.shields.io/badge/Project-Active-success)

An **end-to-end Machine Learning pipeline for Network Security / Intrusion Detection**.
The project automates the workflow of **data ingestion, preprocessing, model training, evaluation, and experiment tracking** using MLflow.

The objective is to **detect malicious network activity** using machine learning models.

---

# 📌 Project Architecture

```
MongoDB
   │
   ▼
Data Ingestion
   │
   ▼
Data Transformation
   │
   ▼
Model Training
   │
   ▼
MLflow Experiment Tracking
   │
   ▼
Saved Model Artifact
```

---

# 📂 Project Structure

```
Network-Security
│
├── artifacts
│
├── Network_Security
│   │
│   ├── components
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── entity
│   │   ├── config_entity.py
│   │   └── artifact_entity.py
│   │
│   ├── constants
│   │
│   ├── logging
│   │
│   ├── exceptions
│   │
│   └── utils
│
├── final_model
│
├── main.py
├── push_data.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Features

✅ Automated **Data Ingestion from MongoDB**
✅ **Feature Store Generation**
✅ **Data Transformation Pipeline**
✅ **Multiple Model Training**
✅ **Automatic Best Model Selection**
✅ **MLflow Experiment Tracking**
✅ **Artifact Generation**
✅ **Production-style ML Pipeline Architecture**

---

# 🤖 Machine Learning Models Used

The pipeline evaluates multiple models:

* Random Forest Classifier
* Decision Tree Classifier
* Gradient Boosting Classifier
* Logistic Regression
* AdaBoost Classifier

The **best performing model** is automatically selected.

---

# 🚀 Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/network-security-ml.git
cd network-security-ml
```

---

### 2️⃣ Create virtual environment

```
python -m venv venv
```

Activate environment:

Mac/Linux

```
source venv/bin/activate
```

Windows

```
venv\Scripts\activate
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

```
MONGO_DB_URL=your_mongodb_connection_string
```

---

# ▶️ Run the Pipeline

Execute the full pipeline:

```
python main.py
```

Pipeline steps:

1️⃣ Data Ingestion from MongoDB
2️⃣ Data Transformation
3️⃣ Model Training
4️⃣ Experiment Tracking (MLflow)
5️⃣ Best Model Saved

---

# 📦 Artifacts Generated

After running the pipeline:

```
artifacts/
   ├── data_ingestion
   │      ├── train.csv
   │      └── test.csv
   │
   ├── data_transformation
   │      ├── train.npy
   │      └── test.npy
   │
   └── model_trainer
          └── model.pkl
```

Final trained model:

```
final_model/model.pkl
```

---

# 🛠 Technologies Used

* Python
* Scikit-learn
* Pandas
* NumPy
* MLflow
* MongoDB
* Logging
* OOP Design

---

# 📈 Future Improvements

* Real-time **network traffic detection**
* **Streamlit dashboard** for predictions
* **FastAPI deployment**
* **Docker containerization**
* **CI/CD pipeline**

---