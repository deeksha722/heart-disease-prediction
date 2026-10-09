# ❤️ Heart Disease Prediction Using Machine Learning

---

## 📌 About the Project

The **Heart Disease Prediction** project aims to predict the possibility of heart disease using patient-related health information and machine learning techniques.

The project involves data exploration, preprocessing, categorical feature encoding, and classification model development. Multiple machine learning algorithms are evaluated, and a trained Random Forest model is saved for integration with a Streamlit web application.

This project demonstrates the application of machine learning concepts to a healthcare-related prediction problem.

## 🎯 Objectives

* 📥 Load and explore heart disease data.
* 🧹 Prepare and preprocess the dataset.
* ⚙️ Encode categorical features for machine learning.
* 📊 Analyze relevant health-related variables.
* 🤖 Train and evaluate classification algorithms.
* 📈 Compare model performance using accuracy.
* 💾 Save the trained Random Forest model.
* 🌐 Develop an interactive prediction interface using Streamlit.

## 🛠️ Technologies Used

| Technology          | Purpose                               |
| ------------------- | ------------------------------------- |
| 🐍 Python           | Programming and implementation        |
| 📓 Jupyter Notebook | Data analysis and model development   |
| 🐼 Pandas           | Data manipulation and preprocessing   |
| 🔢 NumPy            | Numerical operations                  |
| 🤖 Scikit-learn     | Machine learning and model evaluation |
| 📊 Matplotlib       | Data visualization                    |
| 🎨 Seaborn          | Statistical visualization             |
| 🌐 Streamlit        | Interactive web application           |
| 💾 Pickle           | Saving and loading the trained model  |
| 🐙 GitHub           | Project hosting and version control   |

## 📂 Dataset

The project uses a heart disease dataset containing **1,000 records and 16 columns**.

The dataset contains patient-related health information used to explore patterns and train classification models.

Categorical features were encoded during preprocessing, resulting in **22 input features** for model development.

*Note: Refer to the original dataset and notebook for the exact feature names, target variable, and preprocessing details.*

## ⚙️ Project Workflow

### 1️⃣ Data Ingestion

* Loaded the dataset into a Jupyter Notebook.
* Inspected the dataset dimensions, columns, and data types.
* Explored the available health-related features.

### 2️⃣ Data Preprocessing

* Prepared the dataset for machine learning.
* Encoded categorical variables into numerical representations.
* Separated input features and the target variable.
* Prepared the processed data for model training and evaluation.

### 3️⃣ Exploratory Data Analysis (EDA)

* Examined the dataset and its feature distributions.
* Explored relationships between health-related variables.
* Used data analysis and visualization techniques to understand the dataset.

### 4️⃣ Feature Preparation

* Prepared the input features for classification.
* Applied categorical encoding to transform the original features.
* Generated 22 encoded input features for model development.

### 5️⃣ Model Training

The following classification algorithms were explored:

* **Logistic Regression**
* **Decision Tree Classifier**
* **Random Forest Classifier**

These algorithms were used to develop and compare models for predicting heart disease.

### 6️⃣ Model Evaluation

The models were evaluated using classification accuracy.

| Model                    | Observed Accuracy |
| ------------------------ | ----------------: |
| Logistic Regression      |               87% |
| Decision Tree Classifier |              100% |
| Random Forest Classifier |              100% |

*Note: These are the results observed during development. The perfect accuracy scores require further investigation for possible data leakage, train-test overlap, or other evaluation issues. Independent validation is needed before drawing conclusions about model performance.*

### 7️⃣ Model Saving

* Saved the trained Random Forest model using Pickle.
* Stored the model in `heart_disease_rf_model.pkl`.
* Prepared the saved model for use in the Streamlit application.

### 8️⃣ Interactive Application

* Developed a Streamlit interface for user interaction.
* Integrated the saved Random Forest model.
* Enabled predictions based on user-provided health-related inputs.

## 📈 Key Areas of Analysis

The project explores the following areas:

* 🩺 Patterns in patient health-related information.
* 🔍 Relationships among input features.
* ⚙️ The effect of categorical feature encoding on model preparation.
* 🤖 Comparison of different classification algorithms.
* 📊 Evaluation of model performance.
* 🌐 Integration of a machine learning model into a web application.

## 🚀 Getting Started

### Prerequisites

Install Python and the required project dependencies.

### Installation

**1️⃣ Clone the repository**

```bash
git clone <your-github-repository-url>
```

**2️⃣ Navigate to the project directory**

```bash
cd Heart-Disease-Prediction
```

**3️⃣ Install the required libraries**

```bash
pip install -r requirements.txt
```

**4️⃣ Run the Jupyter Notebook**

```bash
jupyter notebook
```

Open your actual notebook filename to explore the data preprocessing and model development workflow.

**5️⃣ Run the Streamlit application**

If your application file is named `app.py`, run:

```bash
streamlit run app.py
```

*Ensure that the required model file and dependencies are available and that the filenames match your repository.*

## 🔮 Future Enhancements

* 🔬 Investigate and improve model generalization.
* 📊 Evaluate models using precision, recall, F1-score, and a confusion matrix.
* 🔄 Apply cross-validation and independent testing.
* ⚙️ Review preprocessing and feature-encoding consistency.
* 🎨 Improve the Streamlit interface and user experience.
* 🌐 Deploy the application for online access.

## 🎓 Learning Outcomes

Through this project, the following concepts were explored:

* Data exploration and preprocessing.
* Categorical feature encoding.
* Classification algorithms in machine learning.
* Model training and performance evaluation.
* Saving and loading trained models.
* Integrating machine learning with Streamlit.
* Developing an end-to-end machine learning project.

## ⚠️ Disclaimer

This project is developed for educational purposes only. Its predictions are not medical diagnoses and must not replace professional medical advice, diagnosis, or treatment. Do not use the application to make medical decisions.

## 👩‍💻 Author

**Deeksha Ravi Kumar**

B.Tech — Computer Science and Engineering
SRM Institute of Science and Technology, Ramapuram

