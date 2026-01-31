import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("laptop_pricing_data.csv")
print("COLUMNS IN DATASET:")
print(df.columns)


# Show first 5 rows
print(df.columns)
print(df.head())

# Dataset info
print(df.info())

# Check missing values
print(df.isnull().sum())

# Basic statistics
print(df.describe())

# Average price by company
avg_price = df.groupby("Brand")["Price_USD"].mean()
print(avg_price)

# Plot
avg_price.plot(kind="bar", figsize=(10,5))
plt.title("Average Laptop Price by Brand")
plt.xlabel("Brand")
plt.ylabel("Price_USD")
plt.show()
