# Used Car Price Prediction

A Machine Learning project that predicts used car selling prices using vehicle specifications and regression algorithms. The project includes data preprocessing, exploratory data analysis, model training, evaluation, and a Streamlit web application.

## Project Overview

Buying or selling a used car can be challenging because prices depend on several factors, including the car's age, current price, mileage, fuel type, transmission, and ownership history.

This project uses historical car data to build a regression model that estimates the selling price of a used car.

## Objectives

- Clean and prepare the dataset.
- Explore relationships between car features and selling prices.
- Train and compare multiple regression models.
- Tune model hyperparameters using GridSearchCV.
- Evaluate model performance using MAE, RMSE, and R².
- Deploy the selected model using Streamlit.

## Dataset

The project uses a CarDekho-style used car dataset containing vehicle information.

**Target variable:** `Selling_Price`

**Features:**
- `Car_Name`: Name of the car
- `Year`: Manufacturing year
- `Present_Price`: Current listed price
- `Kms_Driven`: Distance driven in kilometers
- `Fuel_Type`: Fuel category
- `Seller_Type`: Individual or dealer
- `Transmission`: Manual or automatic
- `Owner`: Number of previous owners

The original dataset contains 301 rows and 9 columns. After removing 2 duplicate rows, the cleaned dataset contains 299 rows.

**Important:** The dataset uses Indian market prices, measured in lakh Indian rupees (INR). The application converts predictions to USD using an approximate exchange rate. Converted prices do not represent actual US market prices.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook
- Git and GitHub

## Project Workflow

1. Data collection and loading
2. Data inspection and preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature and target separation
5. Categorical feature encoding using OneHotEncoder
6. Train-test split
7. Model training and comparison
8. Hyperparameter tuning using GridSearchCV
9. Model evaluation
10. Model serialization using Joblib
11. Deployment with Streamlit

## Machine Learning Models

The project evaluates the following regression algorithms:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Tuned Decision Tree Regressor

The preprocessing steps and regression estimator are combined in Scikit-learn pipelines to ensure consistent transformations during training and prediction.

## Model Evaluation

The models are evaluated using:

- **MAE:** Mean Absolute Error
- **RMSE:** Root Mean Squared Error
- **R²:** Coefficient of Determination

The initial test-set results for Linear Regression were:

| Metric | Result |
|---|---:|
| MAE | 1.411 |
| RMSE | 2.429 |
| R² | 0.771 |

The error metrics are measured in lakh INR, matching the target variable's original unit.

The results are based on a small test set of 60 cars. Performance on other vehicles or markets may differ.

## Streamlit Application

The web application allows users to enter vehicle details and receive an estimated selling price in USD.

### Run Locally

Clone the repository:

```bash
git clone https://github.com/AbdlerahmanGihad/Used-Car-Price-Prediction.git
cd Used-Car-Price-Prediction
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app/app.py
```

Open the local URL displayed in the terminal.

## Project Structure

```text
Used-Car-Price-Prediction/
├── app/
│   └── app.py
├── Data/
│   ├── Raw/
│   │   └── car data.csv
│   └── Processed/
│       └── cleaned_car_data.csv
├── Models/
│   └── best_model.pkl
├── notebooks/
│   ├── 01_preprocessing.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_modeling.ipynb
│   └── 04_evaluation.ipynb
├── Proposals/
├── reports/
│   ├── figures/
│   ├── final_evaluation.csv
│   └── model_comparison.csv
├── .gitignore
├── requirements.txt
└── README.md
```

## Limitations

- The dataset is relatively small.
- Predictions depend on the quality and coverage of the training data.
- The dataset represents the Indian used-car market, not the US market.
- Currency conversion does not account for differences between regional car markets.
- Predictions are estimates and should not be treated as guaranteed market prices.

## Future Improvements

- Test additional regression algorithms.
- Improve feature engineering and model validation.
- Add more recent and diverse vehicle data.
- Improve the Streamlit interface and input validation.
- Use a reliable, up-to-date exchange rate for currency conversion.
- Deploy the application online.

## Author

**Abdelrahman Gihad**

GitHub: [AbdlerahmanGihad](https://github.com/AbdlerahmanGihad)

Project Repository: [Used-Car-Price-Prediction](https://github.com/AbdlerahmanGihad/Used-Car-Price-Prediction)
