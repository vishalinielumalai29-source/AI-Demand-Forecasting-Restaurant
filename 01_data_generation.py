import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os

np.random.seed(42)

# Ensure data folder exists
os.makedirs("data", exist_ok=True)

# 🍽️ Menu items
items = ["Dosa", "Idli", "Burger", "Pizza", "Pasta", "Sandwich", "Biryani"]

categories = {
    "Dosa": "Breakfast",
    "Idli": "Breakfast",
    "Burger": "Fast Food",
    "Pizza": "Fast Food",
    "Pasta": "Italian",
    "Sandwich": "Snacks",
    "Biryani": "Main Course"
}

weather_list = ["Sunny", "Rainy", "Cloudy"]

data = []

start_date = datetime(2025, 1, 1)

# 📅 Generate dataset (1 year)
for i in range(365):
    date = start_date + timedelta(days=i)
    day = date.strftime("%A")

    for item in items:
        price = random.randint(50, 300)
        discount = random.choice([0, 1])
        weather = random.choice(weather_list)

        base_demand = random.randint(60, 220)

        # business logic
        if day in ["Saturday", "Sunday"]:
            base_demand *= 1.4
        if discount == 1:
            base_demand *= 1.3
        if weather == "Rainy":
            base_demand *= 0.85
        if item == "Biryani":
            base_demand *= 1.2

        sales = int(base_demand + np.random.randint(-10, 10))

        data.append([
            date, item, categories[item], day,
            weather, price, discount, sales
        ])

# 📊 Create DataFrame
df = pd.DataFrame(data, columns=[
    "Date", "Item", "Category", "Day",
    "Weather", "Price", "Discount", "Sales"
])

# 💾 Save file
df.to_csv("data/raw_data.csv", index=False)

print("Dataset created successfully!")
print(df.head())
print("Shape:", df.shape)