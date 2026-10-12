import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

st.set_page_config(
    page_title="Used Car Price Prediction",
    page_icon="🚗",
    layout="centered"
)

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "Models" / "best_model.pkl"
DATA_PATH = BASE_DIR / "Data" / "Processed" / "cleaned_car_data.csv"

model = joblib.load(MODEL_PATH)
df = pd.read_csv(DATA_PATH)

INR_TO_USD = 1 / 100

st.title("🚗 Used Car Price Prediction")
st.write("Enter the car details to estimate its selling price in USD.")

car_name = st.selectbox(
    "Car Name",
    sorted(df["Car_Name"].unique())
)

year = st.number_input(
    "Year",
    min_value=int(df["Year"].min()),
    max_value=int(df["Year"].max()),
    value=2017
)

present_price = st.number_input(
    "Present Price (Lakh INR)",
    min_value=0.1,
    max_value=float(df["Present_Price"].max()),
    value=5.0,
    step=0.1
)

kms_driven = st.number_input(
    "Kilometers Driven",
    min_value=0,
    value=30000,
    step=1000
)

fuel_type = st.selectbox(
    "Fuel Type",
    sorted(df["Fuel_Type"].unique())
)

seller_type = st.selectbox(
    "Seller Type",
    sorted(df["Seller_Type"].unique())
)

transmission = st.selectbox(
    "Transmission",
    sorted(df["Transmission"].unique())
)

owner = st.selectbox(
    "Previous Owners",
    sorted(df["Owner"].unique())
)

if st.button("Predict Selling Price"):
    input_data = pd.DataFrame([{
        "Car_Name": car_name,
        "Year": year,
        "Present_Price": present_price,
        "Kms_Driven": kms_driven,
        "Fuel_Type": fuel_type,
        "Seller_Type": seller_type,
        "Transmission": transmission,
        "Owner": owner
    }])

    prediction = model.predict(input_data)[0]

    if prediction < 0:
        st.warning(
            "The model predicted a negative price. "
            "This estimate is not reliable."
        )
    else:
        price_inr = prediction * 100000
        price_usd = price_inr * INR_TO_USD

        st.success(
            f"Estimated Selling Price: ${price_usd:,.2f}"
        )

        st.caption(
            "Price converted from Indian Rupees to USD "
            "using an approximate rate of ₹100 per $1."
        )

        st.caption(
            "This estimate is based on the Indian CarDekho dataset "
            "and does not represent the actual US market price."
        )
