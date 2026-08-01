# 📈 Sales Forecasting using Machine Learning

An end-to-end Machine Learning project that predicts future sales using historical sales data. This project demonstrates the complete machine learning workflow, including data cleaning, exploratory data analysis (EDA), feature engineering, model building, evaluation, and model persistence.

---

# 📌 Project Overview

Sales forecasting is a crucial business task that helps organizations estimate future sales based on historical data. Accurate forecasting supports better inventory management, budgeting, and strategic business planning.

In this project, historical sales data was cleaned, analyzed, and used to train a **Linear Regression** model for predicting future sales. The project includes data preprocessing, exploratory data analysis (EDA), visualization, model training, evaluation, and saving the trained model.

---

# 🎯 Objectives

- Clean and preprocess raw sales data
- Handle missing values and duplicate records
- Perform Exploratory Data Analysis (EDA)
- Create meaningful visualizations
- Build a Machine Learning model for sales prediction
- Evaluate model performance using regression metrics
- Save the trained model for future predictions

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Pandas | Data Cleaning & Data Analysis |
| NumPy | Numerical Computation |
| Matplotlib | Data Visualization |
| Scikit-learn | Machine Learning |
| OpenPyXL | Reading Excel Files |
| Pickle | Saving Trained Model |

---

# 📂 Dataset

The dataset contains historical sales records with the following features:

- 📅 Order Date
- 🌍 Region
- 📦 Product
- 🔢 Quantity
- 💰 Sales
- 📈 Profit

The dataset was cleaned and transformed before training the machine learning model.

---

# 🧹 Data Cleaning

The following preprocessing steps were performed:

- ✅ Removed duplicate records
- ✅ Handled missing values
- ✅ Converted date columns into datetime format
- ✅ Cleaned categorical values
- ✅ Performed feature engineering
- ✅ Prepared the dataset for machine learning

---

# 📊 Exploratory Data Analysis (EDA)

The project includes multiple visualizations to better understand historical sales patterns.

### Visualizations

- 📈 Monthly Sales Trend
- 🌍 Regional Sales Comparison
- 📉 Actual vs Predicted Sales

These visualizations help identify business trends and understand sales performance across different regions.

---

# 🤖 Machine Learning Model

### Model Used

- **Linear Regression**

### Workflow

1. Data Preprocessing
2. Train-Test Split
3. Model Training
4. Sales Prediction
5. Model Evaluation
6. Save the Trained Model using Pickle

---

# 📏 Model Evaluation

The trained **Linear Regression** model was evaluated using standard regression metrics.

| Metric | Value | Description |
|---------|-------------:|-------------|
| **Mean Absolute Error (MAE)** | **94,469.21** | Average absolute difference between actual and predicted sales. |
| **Root Mean Squared Error (RMSE)** | **218,569.01** | Measures prediction error while giving higher weight to larger errors. |
| **R² Score** | **0.8616 (86.16%)** | Indicates that the model explains approximately **86.16%** of the variance in the sales data. |

---

# 📈 Results

The Linear Regression model achieved good predictive performance on the historical sales dataset.

### Model Performance

- ✅ **Mean Absolute Error (MAE):** **94,469.21**
- ✅ **Root Mean Squared Error (RMSE):** **218,569.01**
- ✅ **R² Score:** **0.8616 (86.16%)**

### Interpretation

- The model explains approximately **86.16%** of the variance in the sales data.
- The prediction results closely follow the overall sales trend.
- The model demonstrates good performance for a basic sales forecasting application.

---

# 💡 Business Insights

The exploratory analysis provides several useful business insights:

- Monthly sales trends help identify seasonal demand patterns.
- Regional sales comparison highlights the best-performing regions.
- Actual vs Predicted Sales visualization demonstrates that the model captures overall sales behavior effectively.
- Historical sales analysis can support inventory planning and business decision-making.

---

# 📁 Project Structure

```text
Sales_Forecasting/
│
├── code/
│   ├── Sales_Forecasting.ipynb
│   └── Sales_Forecasting.py
│
├── data/
│   ├── messy_sales_dataset.xlsx
│   └── cleaned_sales_data.xlsx
│
├── images/
│   ├── monthly_sales.png
│   ├── region_sales.png
│   └── actual_vs_predicted.png
│
├── models/
│   └── linear_regression_model.pkl
│
├── README.md
└── requirements.txt
```

---

# ▶️ How to Run the Project

## Clone the Repository

```bash
git clone https://github.com/Manoj007777/Sales_Forecasting.git
```

## Navigate to the Project Directory

```bash
cd Sales_Forecasting
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Project

### Using Jupyter Notebook

Open:

```text
code/Sales_Forecasting.ipynb
```

### Or Run the Python Script

```bash
python code/Sales_Forecasting.py
```

---

# 📦 Requirements

```text
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
- Implement XGBoost Regressor
- Hyperparameter Tuning
- Deploy the project using Streamlit
- Build an interactive dashboard
- Improve prediction accuracy using advanced regression models

---

# 💼 Skills Demonstrated

- Python Programming
- Data Cleaning
- Data Preprocessing
- Exploratory Data Analysis (EDA)
- Data Visualization
- Feature Engineering
- Machine Learning
- Linear Regression
- Model Evaluation
- Model Serialization (Pickle)
- Git & GitHub

---

# 📷 Project Screenshots

Include screenshots of:

- 📈 Monthly Sales Trend
- 🌍 Regional Sales Comparison
- 📉 Actual vs Predicted Sales
- 📊 Model Evaluation Output

---

# 👨‍💻 Author

**Manoj Reddy**

GitHub: https://github.com/Manoj007777

---

## ⭐ If you found this project helpful, please consider giving it a star!
