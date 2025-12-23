import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(10)
# Example dataset
data = {
    'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'sales': [300, 500, 400, 600, 700],
    'profit': [50, 70, 65, 90, 120],
    'expenses': np.random.randint(100,200,5)
}
df = pd.DataFrame(data)
#print(df)

#line plot
fig, ax=plt.subplots(figsize=(12,8))
df.plot(x='month', y='sales', marker='o', markeredgecolor='green', color='blue', lw=2, ls='--',  ax=ax)
ax.set_title("Monthly Sales Trend")
ax.set_xlabel("Month")
ax.set_ylabel("Sales ($)")
plt.show()

#multiple line on same graph
df.plot(x='month', y=['sales','profit'], marker='o', markeredgecolor='green', color=['blue','purple'], lw=2, ls='--')
plt.show()

#bar plot
df.plot(kind='bar', x='month', y='sales')
plt.title("Monthly Sales (Bar Chart)")
plt.show()

#histogram
df['sales'].plot(kind='hist', bins=10, color='blue')  
plt.show()

#scatter
df.plot(kind='scatter', x='sales', y='profit', color='blue')
plt.show()

#box plot
df[['sales', 'profit', 'expenses']].plot(kind='box')
plt.title("Box Plot of Sales, Profit, and Expenses")
plt.show()

#area plot
df.plot(x='month', y=['sales', 'expenses'], kind='area', alpha=0.5)
plt.title("Sales vs Expenses Over Time (Area Plot)")
plt.show()

#pie
df.set_index('month')['sales'].plot(kind='pie', autopct='%1.1f%%', figsize=(6,6))
plt.title("Sales Share by Month")
plt.ylabel('')  # Remove ylabel for clean look
plt.show()

#kde
df['expenses']=df['expenses'].astype('float')
df['expenses'].plot(kind='kde', color='green')
plt.title("Profit Distribution (KDE)")
plt.show()

#subPlots--many charts in one figure
df[['sales', 'profit', 'expenses']].plot(kind='line', subplots=True, layout=(3,1), figsize=(8,8))
plt.suptitle("Company Performance Overview")
plt.show()

#combine multiple plots(important***)
ax = df.plot(x='month', y='sales', kind='bar', color='skyblue', figsize=(8,5))
df.plot(x='month', y='profit', kind='line', color='red', marker='o', ax=ax)
plt.title("Sales (Bar) and Profit (Line)")
plt.show()

#REAL WORLD WORKFLOW
# 1. Overview trends
df.plot(x='month', y=['sales','profit','expenses'], kind='line', figsize=(10,5))

# 2. Check distributions
df[['sales','profit']].plot(kind='hist', alpha=0.6, bins=10, figsize=(8,5))

# 3. Correlations
df.plot(kind='scatter', x='sales', y='profit')

plt.show()







