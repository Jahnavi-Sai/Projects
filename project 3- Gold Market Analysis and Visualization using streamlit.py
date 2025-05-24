import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🪙💰 Gold Price Visualization ")

df = pd.read_csv(r"C:\Users\91630\Downloads\gold_price_3_years.csv", parse_dates=["date"])

# Fix grams to 10 and filter date range
df['grams'] = 10
df = df[(df['date'] >= '2023-01-01') & (df['date'] <= '2025-12-31')]

first_date, last_date = df['date'].iloc[0], df['date'].iloc[-1]

date = st.date_input("Select date", value=first_date, min_value=first_date, max_value=last_date)
grams = st.number_input("Grams", min_value=0.1, value=10.0, step=0.1)

price_row = df[df['date'] == pd.to_datetime(date)]
price = price_row['price'].values[0]
calc_price = price / 10 * grams

st.metric(f"Price for {grams}g", f"₹{calc_price:,.2f}")

fig, ax = plt.subplots()
ax.plot(df['date'], df['price'], color='gold', linewidth=2)
ax.scatter(date, price, color='red', s=100)
ax.set_title("Gold Price Trend (2023-2025)")
ax.set_ylabel("Price (₹)")
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(fig)
