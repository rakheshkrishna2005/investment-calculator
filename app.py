import streamlit as st
import pandas as pd
import numpy as np

# Title and header
st.title("Investment Calculator")

github_button = st.sidebar.button("GitHub Repository")

# Check if the buttons were clicked
if github_button:
    st.sidebar.markdown("[Visit GitHub Repository](https://github.com/rakheshkrishna2005/investment-calculator)")

# Sidebar for selecting the calculator type
option = st.sidebar.selectbox("Choose Investment Type", ["SIP Calculator", "Lumpsum Calculator"])

if option == "SIP Calculator":
    st.write("### SIP Calculator")
    
    # SIP Inputs
    monthly_investment = st.number_input("Monthly Investment Amount", min_value=0, value=1000)
    annual_interest_rate = st.number_input("Annual Interest Rate (in %)", min_value=0.0, value=12.0)
    investment_duration_years = st.number_input("Investment Duration (in years)", min_value=1, value=1)
    
    # Convert annual interest rate to monthly and calculate SIP returns
    monthly_rate = annual_interest_rate / 100 / 12
    number_of_payments = investment_duration_years * 12
    future_value = monthly_investment * (((1 + monthly_rate) ** number_of_payments - 1) / monthly_rate) * (1 + monthly_rate)
    total_investment = monthly_investment * number_of_payments
    estimated_returns = future_value - total_investment
    
    st.write(f"### SIP Investment Details")
    st.write(f"**Invested Amount**: ₹{total_investment:,.2f}")
    st.write(f"**Estimated Returns**: ₹{estimated_returns:,.2f}")
    st.write(f"**Total Value**: ₹{future_value:,.2f}")
    
    # Display a simple chart
    periods = np.arange(1, number_of_payments + 1)
    values = monthly_investment * (((1 + monthly_rate) ** periods - 1) / monthly_rate) * (1 + monthly_rate)
    
    st.line_chart(pd.DataFrame(values, columns=["Value"], index=periods))

elif option == "Lumpsum Calculator":
    st.write("### Lumpsum Calculator")
    
    # Lumpsum Inputs
    lumpsum_investment = st.number_input("Lumpsum Investment Amount", min_value=0, value=10000)
    annual_interest_rate = st.number_input("Annual Interest Rate (in %)", min_value=0.0, value=12.0)
    investment_duration_years = st.number_input("Investment Duration (in years)", min_value=1, value=1)
    
    # Convert annual interest rate to annual compound interest and calculate lumpsum returns
    annual_rate = annual_interest_rate / 100
    future_value = lumpsum_investment * ((1 + annual_rate) ** investment_duration_years)
    estimated_returns = future_value - lumpsum_investment
    
    st.write(f"### Lumpsum Investment Details")
    st.write(f"**Invested Amount**: ₹{lumpsum_investment:,.2f}")
    st.write(f"**Estimated Returns**: ₹{estimated_returns:,.2f}")
    st.write(f"**Total Value**: ₹{future_value:,.2f}")
    
    # Display a simple chart
    periods = np.arange(1, investment_duration_years + 1)
    values = lumpsum_investment * ((1 + annual_rate) ** periods)
    
    st.line_chart(pd.DataFrame(values, columns=["Value"], index=periods))