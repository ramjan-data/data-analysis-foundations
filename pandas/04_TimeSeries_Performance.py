#baseline setup
import pandas as pd
df = pd.read_csv("sales_orders.csv", parse_dates=["order_date"])
df["discount"] = df["discount"].fillna(0)
df["total_price"] = df["quantity"] * df["unit_price"]
df["final_price"] = df["total_price"] * (1 - df["discount"])


"""Time Series-"""
#converting text into datetime
date='2025-09-17'
df=pd.to_datetime(date)
print(df)

dates = ['2025-09-17', '17/09/2025', 'Sep 17 2025']

dff=pd.to_datetime(dates, errors="coerce")
print(dff)

drange=pd.date_range(start='2025-01-01', end='2025-01-10', freq='2D')  #D,H,M(month end),MS(month start),W,Y,B(monday-friday only),
print(drange)


#Datetime Accessors (.dt)
df["year"] = df["order_date"].dt.year
df["month"] = df["order_date"].dt.month
df["day"] = df["order_date"].dt.day
df["weekday"] = df["order_date"].dt.day_name()

#Set Datetime as Index
df = df.set_index("order_date").sort_index()


#Time-Based Slicing
df.loc["2023-01"]
df.loc["2023-01-10":"2023-02-10"]


"""Resampling (Time-Series Aggregation):
                    Common frequencies:
                                    D day
                                    W week
                                    M month
                                    Q quarter
                                    Y year

"""
#monthly revenue
df['final_price'].resample('M').sum()

#Weekly average order
df["final_price"].resample("W").mean()

#multiple aggregation
mres=df.resample('M').agg({'value' : ['sum','mean','max']})


#timedelta
now = pd.Timestamp('2025-09-17')
past = pd.Timestamp('2025-09-10')
diff = now - past
print(diff.days)           # 7



""""Rolling Windows (Trends)"""
#3-order moving average
df["rolling_avg"] = df["final_price"].rolling(window=3).mean()



"""Categorical DATA
Why category Matters:
                    Object dtype-slow
                                -Memory heavy

                    Category dtype-Encoded integers
                                  -Faster groupby
                                  -Less memory
"""

#Convert to Category
df["region"] = df["region"].astype("category")
df["category"] = df["category"].astype("category")
#check
df.info()


#Category Operations
# print(cat_data.cat.categories)  #checking unique categories
# cat_data=cat_data.cat.rename_categories({'male':'M','female':'F', 'others':'O'})   #renaming the categories
# cat_data=cat_data.cat.add_categories(['unknown'])                 #add new category
# cat_data=cat_data.cat.remove_categories(['O'])   

df["region"].cat.categories
df["region"].cat.codes

#rename
df["region"] = df["region"].cat.rename_categories({
    "Asia": "ASIA",
    "Europe": "EU",
    "America": "US"
})


#Memory Optimization
df.memory_usage(deep=True)    #Check Memory Usage

#Downcast Numerics
df["quantity"] = pd.to_numeric(df["quantity"], downcast="integer")
df["unit_price"] = pd.to_numeric(df["unit_price"], downcast="float")


