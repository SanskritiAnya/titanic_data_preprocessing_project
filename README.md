# 🚢 Titanic Data Preprocessing Project

This project involves comprehensive **data preprocessing** on the famous **Titanic dataset**, a classic dataset used in data science and machine learning. The goal is to prepare the data for model building by cleaning, transforming, and scaling it.

---

## 📌 Project Overview

The Titanic dataset contains information about passengers aboard the Titanic. The preprocessing steps performed in this project are crucial to ensure the dataset is clean, consistent, and suitable for machine learning models.

---

## ✅ Key Steps Performed

### 1. 📊 Data Exploration
- Displayed basic information: data types, null values, and dataset structure
- Analyzed distributions and value counts for key columns

### 2. ❓ Handling Missing Values
- Filled missing values in the `Age` column using the median
- Dropped the `Cabin` column due to excessive null values
- Imputed missing `Embarked` values using the mode

### 3. 🔤 Encoding Categorical Variables
- Converted `Sex` to numerical format (`male = 0`, `female = 1`)
- Used one-hot encoding for the `Embarked` column with `pd.get_dummies()`

### 4. ⚖️ Feature Scaling
- Applied **Min-Max Normalization** (values scaled to [0, 1])
- Applied **Standardization** (mean = 0, standard deviation = 1)
- Scaled columns: `Age`, `Fare`, `SibSp`, `Parch`, `Pclass`

### 5. 📉 Outlier Detection
- Visualized outliers in numerical features using boxplots
- Identified and removed outliers beyond acceptable IQR range

---

## 🛠️ Tools & Libraries Used

- **Python 3**
- **Pandas** – Data manipulation
- **NumPy** – Numerical computation
- **Matplotlib & Seaborn** – Visualization
- **Scikit-learn** – Scaling methods

---

## 📁 Project Structure

titanic-data-preprocessing/
│
├── titanic-dataset.zip # Raw dataset
├── titanic_preprocessing.ipynb # Main preprocessing notebook
├── README.md # Project documentation


---

## 🎯 Goal

To obtain a clean, scaled, and outlier-free dataset ready for machine learning models like logistic regression, decision trees, or random forests.

---

## 🙌 Acknowledgements

Dataset source: [Kaggle - Titanic: Machine Learning from Disaster](https://www.kaggle.com/c/titanic)

---

## 📬 Contact

For questions or feedback, feel free to connect:

**Sanskriti Anya**  
📧 sanskritianya17@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/sanskriti-anya-6bb2b4332)
