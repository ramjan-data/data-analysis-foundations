"""Professional EDA Workflow"""
#Step 1: Load + Validate
import pandas as pd
df=pd.read_csv(r"C:\Users\USER\OneDrive\Desktop\python\sales_orders.csv")
df.info()

#Step 2: Structural Sanity Checks
df.head()
df.tail()
df.sample(5)
df.nunique()

#Step 3: Data Quality Checks
df.isna().sum()
df.duplicated().sum()

#Validate business logic
(df["quantity"] <= 0).sum()
(df["unit_price"] <= 0).sum()


#Feature Engineering 
df["revenue"] = df["quantity"] * df["unit_price"] * (1 - df["discount"].fillna(0))
df["is_returned"] = df["returned"].astype(int)  #flag
df["order_month"] = df["order_date"].dt.to_period("M") #Time-based features



#Exploratory Analysis (Decision-Oriented)
#revenue by region
df.groupby("region")["revenue"].sum().sort_values(ascending=False)

#return rate
df.groupby("category")["is_returned"].mean()

#monthly trend
df.set_index("order_date")["revenue"].resample("M").sum()



"""Performance Checklist (Memorize):
                    
                    Before scaling:
                                -Convert object → category
                                -Downcast numerics
                                -Reduce columns early
                                -Avoid apply
                                -Group once, aggregate many
                                -Use Parquet, not CSV

"""

