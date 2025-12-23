import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go


# Create data
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
categories = ['Electronics', 'Clothing', 'Home Decor', 'Toys']

np.random.seed(42)
data = {
    'month': np.tile(months, len(categories)),
    'category': np.repeat(categories, len(months)),
    'sales': np.random.randint(20000, 80000, len(months)*len(categories)),
    'profit': np.random.randint(2000, 10000, len(months)*len(categories)),
    'rating': np.round(np.random.uniform(3.0, 5.0, len(months)*len(categories)), 1)
}
df = pd.DataFrame(data)
print(df.head())


#scatter
fig=px.scatter(df, x='sales', y='profit', color='category',size='rating', hover_data=['month'], title='Sales vs Profit by Category')
fig.show()

#line 
avg_sales = df.groupby('month', sort=False)['sales'].mean().reset_index()
fig = px.line(avg_sales, x='month', y='sales', markers=True, title='Average Monthly Sales Trend')
fig.show()

#bar
cat_sales = df.groupby('category', as_index=False)['sales'].sum()
fig = px.bar(cat_sales, x='category', y='sales', color='category', title='Total Sales by Product Category')
fig.show()

#pie
cat_profit = df.groupby('category', as_index=False)['profit'].sum()
fig = px.pie(cat_profit, names='category', values='profit', title='Profit Contribution by Category',  hole=0.1 ) # makes it a donut chart 
fig.show()

#datests
#print(px.data.__all__)










