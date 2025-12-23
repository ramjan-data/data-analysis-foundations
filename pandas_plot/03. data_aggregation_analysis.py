import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(10)
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
regions = ['East', 'West', 'North', 'South']
categories = ['Electronics', 'Clothing', 'Furniture']

# Simulated dataset
df = pd.DataFrame({
    'Month': np.random.choice(months, 100),
    'Region': np.random.choice(regions, 100),
    'Category': np.random.choice(categories, 100),
    'Sales': np.random.randint(500, 5000, 100),
    'Profit': np.random.randint(50, 1000, 100),
    'Quantity': np.random.randint(1, 20, 100)
})
print(df.head())

#grouping and aggregation data
# ex-1: sales  by region
region_sales=df.groupby('Region')['Sales'].sum()
region_sales.plot(kind='bar', color='teal', figsize=(10,6))
plt.title("Total Sales by Region")
plt.ylabel("Sales ($)")
plt.show()

#ex-2: Average Profit by Category
cat_profit = df.groupby('Category')['Profit'].mean().sort_values(ascending=False)
cat_profit.plot(kind='barh', color='blue', figsize=(10,6))
plt.title("Average Profit by Category")
plt.xlabel("Profit ($)")
plt.show()

#ex-3: Monthly Sales Trend
monthly_sales = df.groupby('Month')['Sales'].sum().reindex(months)
monthly_sales.plot(kind='line', marker='o', figsize=(8,5))
plt.title("Monthly Sales Trend")
plt.ylabel("Total Sales ($)")
plt.grid(True)
plt.show()

#ex-4:group by multiple rows
region_cat = df.groupby(['Region','Category'])['Sales'].sum().unstack()
region_cat.plot(kind='bar', figsize=(9,5))
plt.title("Sales by Region and Category")
plt.ylabel("Sales ($)")
plt.show()

#ex-5:Pivot Tables + Plots
pivot_sales = pd.pivot_table(df, values='Sales', index='Month', columns='Region', aggfunc='sum').reindex(months)
pivot_sales.plot(kind='area', figsize=(10,6), alpha=0.6)
plt.title("Monthly Sales by Region (Area Plot)")
plt.ylabel("Sales ($)")
plt.show()


#cumulative sales
df_sorted = df.groupby('Month')['Sales'].sum().reindex(months)
df_sorted.cumsum().plot(kind='line', marker='o', figsize=(8,4))
plt.title("Cumulative Sales Over Months")
plt.ylabel("Cumulative Sales ($)")
plt.grid(True)
plt.show()

#rolling
df_sorted.rolling(3).mean().plot(kind='line', color='green', marker='o')
plt.title("3-Month Rolling Average of Sales")
plt.ylabel("Avg Sales ($)")
plt.grid(True)
plt.show()




