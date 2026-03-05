# 🌍 Air Quality Monitoring System using Machine Learning

## 📌 Project Overview

The **Air Quality Monitoring System** is a web-based application that predicts air quality levels using a Machine Learning model. The system analyzes environmental parameters and predicts the **Air Quality Index (AQI)** to help users understand pollution levels in real time.

This project integrates **Machine Learning with a web application built using Django**, allowing users to input environmental parameters and receive air quality predictions instantly.

---

## 🚀 Features

* Predicts **Air Quality Index (AQI)** using a trained ML model
* User-friendly **web interface** built with Django
* Machine Learning model trained with environmental data
* Real-time prediction based on user input
* Simple and responsive UI
* Model accuracy of **above 80%**

---

## 🧠 Machine Learning Model

The system uses a trained **Machine Learning regression model** to predict air quality levels.

### Model Workflow

1. Data Collection
2. Data Preprocessing
3. Feature Selection
4. Model Training
5. Model Evaluation
6. Deployment with Django

### Model Performance

* **Algorithm Used:** Machine Learning Regression Model
* **Accuracy Achieved:** **80%+ prediction accuracy**

The trained model is stored as:

```id="c6f6u7"
model.pkl
```

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Framework

* Django

### Machine Learning

* Scikit-learn
* Pandas
* NumPy

### Frontend

* HTML
* CSS

### Database

* SQLite

---

## 📂 Project Structure

```id="n7s3v8"
AIE/
│
├── air_quality/
│   ├── air_quality/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │
│   ├── predictor/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── templates/
│   │       └── index.html
│   │
│   ├── model.pkl
│   ├── manage.py
│   └── db.sqlite3
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```id="9x5g2r"
git clone https://github.com/makhila-2005/Air-Quality-Monitoring-System-Updated-.git
```

---

### 2️⃣ Navigate to the project folder

```id="p4t0k1"
cd AIE
```

---

### 3️⃣ Create virtual environment

```id="5y3f0q"
python -m venv venv
```

---

### 4️⃣ Activate virtual environment

**Windows**

```id="r3p4q1"
venv\Scripts\activate
```

---

### 5️⃣ Install required libraries

```id="2w6f1z"
pip install django scikit-learn pandas numpy
```

---

### 6️⃣ Run the server

```id="z8y3h5"
python manage.py runserver
```

---

### 7️⃣ Open in Browser

```id="v6q2k4"
http://127.0.0.1:8000
```

---

## 📊 System Workflow

1️⃣ User enters environmental parameters
2️⃣ Input data is sent to Django backend
3️⃣ Backend loads **trained ML model (`model.pkl`)**
4️⃣ Model predicts **Air Quality Index**
5️⃣ Result is displayed on the web interface

---

## 🔮 Future Improvements

* Real-time sensor data integration
* IoT-based air quality monitoring
* Graphical data visualization
* Mobile application integration
* Cloud deployment

---

## 👩‍💻 Author

**Akhila Mulukutla**

---

## 📜 License

This project is developed for educational and research purposes.
