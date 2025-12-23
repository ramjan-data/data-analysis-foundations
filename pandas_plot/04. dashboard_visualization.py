import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

np.random.seed(42)
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
regions = ['East','West','North','South']
categories = ['Electronics','Clothing','Furniture']

df = pd.DataFrame({
    'Month': np.random.choice(months, 200),
    'Region': np.random.choice(regions, 200),
    'Category': np.random.choice(categories, 200),
    'Sales': np.random.randint(500, 8000, 200),
    'Profit': np.random.randint(50, 2000, 200),
    'Discount': np.random.uniform(0, 0.3, 200)
})
print(df.head())

#interective visuals with plotly
#Sales vs Profit (Interactive Scatter)
fig = px.scatter(
    df, x='Sales', y='Profit', color='Category',
    size='Discount', hover_data=['Region','Month'],
    title='Sales vs Profit (Interactive)'
)
fig.show()

#Sales by Region (Interactive Bar)
fig = px.bar(
    df.groupby('Region')['Sales'].sum().reset_index(),
    x='Region', y='Sales', color='Region', title='Total Sales by Region'
)
fig.show()

#Monthly Sales Trend (Line)
monthly_sales = df.groupby('Month')['Sales'].sum().reindex(months).reset_index()
fig = px.line(monthly_sales, x='Month', y='Sales', markers=True, title='Monthly Sales Trend (Interactive)')
fig.show()



#Dashboard Layout with Subplots (Professional Style)
fig, axs = plt.subplots(2, 2, figsize=(14,8))

# Plot 1 – Total Sales by Region
df.groupby('Region')['Sales'].sum().plot(kind='bar', ax=axs[0,0], color='skyblue')
axs[0,0].set_title('Total Sales by Region')

# Plot 2 – Average Profit by Category
df.groupby('Category')['Profit'].mean().plot(kind='barh', ax=axs[0,1], color='salmon')
axs[0,1].set_title('Average Profit by Category')

# Plot 3 – Sales Distribution Histogram
df['Sales'].plot(kind='hist', bins=15, color='limegreen', ax=axs[1,0])
axs[1,0].set_title('Sales Distribution')

# Plot 4 – Profit Trend (Line)
profit_trend = df.groupby('Month')['Profit'].sum().reindex(months)
profit_trend.plot(ax=axs[1,1], color='purple', marker='o')
axs[1,1].set_title('Monthly Profit Trend')

plt.suptitle("Business Performance Dashboard", fontsize=18, fontweight='bold')
plt.tight_layout()
plt.show()



#correlation heatmap
corr = df[['Sales','Profit','Discount']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()


