
<h1>Titanic Passenger Survival Prediction Using Machine Learning</h1>

🧾Summary:

✅Predict whether a passenger survived the Titanic disaster using supervised machine learning models.

📖 Overview

✅This project builds a machine learning pipeline to analyze Titanic passenger data and predict survival outcomes. It covers data cleaning, exploratory data analysis (EDA), feature engineering, model training, and evaluation. The goal is not just prediction, but understanding which factors actually mattered.

❓ Problem Statement

Given passenger information such as age, gender, ticket class, fare, and family size, predict whether the passenger survived the Titanic disaster.

This is a binary classification problem:

1 → Survived

0 → Did not survive

📊 Dataset

✅Source:<a href="https://github.com/rajan-kumar-mu1439/titanic-survival-prediction-ml/blob/main/Titanic-Dataset.csv">Titanic passengers Dataset</a>

Rows: 891 passengers

Target Variable: Survived

🔑 Key Features:

✅Pclass – Passenger class (1st, 2nd, 3rd)

✅Sex – Gender

✅Age – Passenger age

✅SibSp – Siblings / spouses aboard

✅Parch – Parents / children aboard

✅Fare – Ticket fare

🛠️ Tools & Technologies

✅Language: Python 🐍

👉Libraries:

✅pandas, numpy – Data handling

✅matplotlib, seaborn – Visualization

✅scikit-learn – ML models & preprocessing

✅Environment: Jupyter Notebook

⚙️ Methods & Workflow

1️⃣ Data Preprocessing

✅Handled missing values (Age, Embarked)

✅Dropped irrelevant columns (Cabin, Ticket, Name if unused)

✅Encoded categorical variables (Sex, Embarked)

✅Feature scaling where required

✅Skipping preprocessing = garbage-in, garbage-out.

2️⃣ Exploratory Data Analysis (EDA)

✅Survival rate by gender

✅Survival vs passenger class

✅Age and fare distribution analysis

3️⃣ Model Building

✅Trained and evaluated models such as:

✅Logistic Regression

✅Used train-test split to avoid overfitting.

4️⃣ Model Evaluation

✅Accuracy score

✅Confusion matrix

📌 Key Insights

✅Women had significantly higher survival rates

✅First-class passengers were prioritized

✅Higher fare correlated with better survival chances

✅Alone passengers had lower survival probability

📈 Output / Model Results

✅Best model achieved reasonable accuracy on test data

✅Predictions generated for unseen samples

📉 No model here is production-ready. This is a learning project — treat it honestly.

▶️ How to Run This Project

Clone the repository

git clone https://github.com/rajan-kumar-mu1439/titanic-survival-prediction-ml

Navigate to the project folder

cd titanic-survival-prediction-ml

Install dependencies

pip install python, numpy, pandas, matplotlib, seaborn, Scikit learn

Open Jupyter Notebook

jupyter notebook

Run titanic_prediction.ipynb step by step

👉 Results & Conclusion

✅The project successfully demonstrates how machine learning can be applied to structured historical data for classification tasks. More importantly, it shows how social factors influence outcomes, not just algorithms.

🔮 Future Work

✅Hyperparameter tuning

✅Cross-validation

✅Feature engineering (family size, title extraction)

✅Compare advanced models (XGBoost, Gradient Boosting)

✅Deploy as a web app (Flask / Streamlit)

👤 Author & Contact

Rajan Kumar

Python Developer | Data Analytics & Machine Learning

📧 Email: rajankumarmu1439@gmail.com

🔗 LinkedIn:  https://www.linkedin.com/in/rajan-kumar-mu1439/
