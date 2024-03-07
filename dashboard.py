import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data into a DataFrame
df = pd.read_csv("day.csv")
df = pd.read_csv("hour.csv")

# Sidebar
st.sidebar.title("Menu")
view_data = st.sidebar.checkbox("View Data")

# Main content
st.title("Bike Sharing Dashboard")

if view_data:
    st.subheader("Raw Data")
    st.write(df)

# Visualizations
st.subheader("Visualizations")

# Count of rented bikes by season
st.write("Count of rented bikes by season")
season_counts = df.groupby('season')['cnt'].sum()
st.bar_chart(season_counts)

# Comparison of registered and casual users
st.write("Comparison of registered and casual users")
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='hr', y='casual', label='Casual')
sns.lineplot(data=df, x='hr', y='registered', label='Registered')
plt.xlabel("Hour")
plt.ylabel("Count")
plt.title("Comparison of Registered and Casual Users by Hour")
plt.legend()
st.pyplot(plt)

# Analysis: In which season are fewer bikes rented?
st.subheader("In which season are fewer bikes rented?")
season_average = df.groupby('season')['cnt'].mean()
min_season = season_average.idxmin()
st.write(f"The season with the fewest bike rentals on average is {min_season}")