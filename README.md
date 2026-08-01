# 📈 Sales Forecasting using Machine Learning

An end-to-end Machine Learning project that predicts future sales using historical sales data. This project demonstrates the complete machine learning workflow, including data cleaning, exploratory data analysis (EDA), feature engineering, model building, evaluation, and model deployment preparation.

---

# 📌 Project Overview

Sales forecasting helps businesses estimate future sales based on historical data, enabling better inventory management, budgeting, and business planning.

In this project, raw sales data was cleaned and preprocessed before training a **Linear Regression** model to predict future sales. Various visualizations were created to analyze sales trends, regional performance, and model predictions.

---

# 🎯 Objectives

- Clean and preprocess raw sales data
- Handle missing values and duplicate records
- Perform Exploratory Data Analysis (EDA)
- Create meaningful visualizations
- Train a Machine Learning model for sales prediction
- Evaluate model performance using regression metrics
- Save the trained model for future predictions

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Pandas | Data Cleaning & Analysis |
| NumPy | Numerical Computation |
| Matplotlib | Data Visualization |
| Scikit-learn | Machine Learning |
| OpenPyXL | Reading Excel Files |
| Pickle | Model Saving |

---

# 📂 Dataset

The dataset contains historical sales information with features such as:

- 📅 Order Date
- 🌍 Region
- 📦 Product
- 🔢 Quantity
- 💰 Sales
- 📈 Profit

The dataset was cleaned and transformed before being used for model training.

---

# 🧹 Data Cleaning

The following preprocessing steps were performed:

- ✅ Removed duplicate records
- ✅ Handled missing values
- ✅ Converted date columns into datetime format
- ✅ Cleaned categorical values
- ✅ Performed feature engineering
- ✅ Prepared data for machine learning

---

# 📊 Exploratory Data Analysis (EDA)

The project includes several visualizations to understand sales patterns.

### Visualizations

- 📈 Monthly Sales Trend
- 🌍 Regional Sales Comparison
- 📦 Product-wise Sales Analysis
- 📊 Sales Distribution
- 📉 Actual vs Predicted Sales
- 📦 Box Plot for Outlier Detection

These visualizations provide meaningful insights into historical sales performance.

---

# 🤖 Machine Learning Model

### Model Used

- Linear Regression

### Workflow

1. Split dataset into training and testing sets
2. Train the Linear Regression model
3. Predict sales on the test dataset
4. Evaluate model performance
5. Save the trained model using Pickle

---

# 📏 Model Evaluation

The model is evaluated using the following metrics:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score (Coefficient of Determination)

These metrics help measure the prediction accuracy of the model.

---

# 📈 Results

The trained Linear Regression model successfully predicts future sales based on historical sales data.

The project demonstrates the complete machine learning workflow from raw data preprocessing to prediction and model saving.

---

# 💡 Business Insights

Some useful insights obtained from the analysis include:

- Monthly sales trends help identify seasonal demand.
- Regional sales comparison highlights the best-performing regions.
- Product-wise analysis identifies top-selling products.
- Actual vs Predicted visualization helps evaluate model performance.
- Data visualization supports better business decision-making.

---

# 📁 Project Structure

```
Sales_Forecasting/
│
├── data/
│   ├── messy_sales_dataset.xlsx
│   └── cleaned_sales_dataset.xlsx
│
├── notebooks/
│   └── Sales_Forecasting.ipynb
│
├── models/
│   └── linear_regression_model.pkl
│
├── images/
│   ├── monthly_sales.png
│   ├── regional_sales.png
│   ├── product_sales.png
│   └── actual_vs_predicted.png
│
├── requirements.txt
│
└── README.md
```

---

# ▶️ How to Run the Project

## Clone the repository

```bash
git clone https://github.com/Manoj007777/Sales_Forecasting.git
```

## Navigate to the project folder

```bash
cd Sales_Forecasting
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run the notebook

Open the notebook using Jupyter Notebook or Google Colab:

```
notebooks/Sales_Forecasting.ipynb
```

Run all cells to reproduce the complete workflow.

---

# 📦 Requirements

```
pandas
numpy
matplotlib
scikit-learn
openpyxl
```

---

# 🚀 Future Improvements

- Implement Decision Tree Regression
- Implement Random Forest Regression
- Try XGBoost Regressor
- Perform Hyperparameter Tuning
- Deploy the model using Streamlit
- Build an interactive dashboard
- Add Time Series Forecasting models
- Improve prediction accuracy using advanced algorithms

---

# 💼 Skills Demonstrated

- Python Programming
- Data Cleaning
- Data Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Data Visualization
- Machine Learning
- Linear Regression
- Model Evaluation
- Model Serialization
- Git & GitHub

---

# 📷 Project Screenshots

Add screenshots of:

- Monthly Sales Trend
- Regional Sales Comparison
- Product-wise Sales
- Actual vs Predicted Sales
- Model Evaluation Output

These screenshots make the repository more attractive to recruiters.

---

# 👨‍💻 Author

**Manoj Reddy**

GitHub: https://github.com/Manoj007777

---

## ⭐ If you found this project helpful, please consider giving it a star!
