import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Simulated real-world data
data = {
    'Month': ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
    'Revenue': [12000, 15000, 18000, 22000, 25000, 23000, 27000, 30000, 28000, 35000, 37000, 40000],
    'Profit': [2000, 2500, 2600, 3500, 4200, 4000, 5000, 5500, 4800, 6200, 6400, 7000],
    'Expenses': [8000, 9000, 10000, 13000, 14000, 13500, 15000, 16000, 15000, 18000, 19000, 20000]
}
df = pd.DataFrame(data)
#print(df.head())


#customize and styling
fig, ax= plt.subplots()
plt.style.use('seaborn-v0_8-darkgrid')  #apply different style(others are- ggplot, bmh, fivethirtyeight)
df.plot(x='Month', y=['Revenue','Profit','Expenses'], kind='line', marker='o', figsize=(10,5), ax=ax)
ax.set_title("Monthly Revenue Growth", fontsize=16, fontweight='bold', color='darkblue')
ax.set_xlabel("Month", fontsize=12)
ax.set_ylabel("Revenue ($)", fontsize=12)
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend(title='Metrices', loc='upper right')
plt.show()

#bar chart customization(colors, rotatiions)
df.plot(kind='bar', x='Month', y=['Revenue', 'Expenses'], figsize=(10,6), color=['blue','purple'])
plt.title("Monthly Revenue vs Expenses", fontsize=15)
plt.xlabel("Month")
plt.ylabel("Amount ($)")
plt.xticks(rotation=45)
plt.legend(title="Metrics")
plt.tight_layout()
plt.show()




