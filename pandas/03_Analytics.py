import pandas as pd
df=pd.read_csv(r"C:\Users\USER\OneDrive\Desktop\python\sales_orders.csv")
print(df.head())

#previous works
df["discount"] = df["discount"].fillna(0)
df["total_price"] = df["quantity"] * df["unit_price"]
df["final_price"] = df["total_price"] * (1 - df["discount"])


"""Groupby"""
#Total Sales per region
salesBy_region=df.groupby('region')['final_price'].sum()

#Mean order value per category
category_mean_price=df.groupby("category")["final_price"].mean()

#multiple aggregation
region_agg=df.groupby("region")["final_price"].agg(["sum", "mean", "count"])

#Rename cleanly
df.groupby("region").agg(
    total_sales=("final_price", "sum"),
    avg_order=("final_price", "mean"),
    orders=("order_id", "count")
)

#Grouping by Multiple Columns
df.groupby(["region", "category"]).agg(
    revenue=("final_price", "sum"),
    qty=("quantity", "sum")
)


#groupby + Filtering (HAVING)
region_sales = df.groupby("region")["final_price"].sum()
region_sales[region_sales > 3000]


#transform : returns same shape as original DataFrame.(like sql window function)
df["region_avg"] = df.groupby("region")["final_price"].transform("mean")
df["above_region_avg"] = df["final_price"] - df["region_avg"]




"""Pivot table"""
pivot_t1=pd.pivot_table(df, values="final_price", index="region", columns="category", aggfunc="sum",  fill_value=0)
pivot_t2=pd.pivot_table( df, values="final_price", index="region", columns="category", aggfunc="sum",  margins=True)


"""Reshaping Data"""
#melt (Wide → Long)
melt=pd.melt( df,  id_vars=["order_id", "region"],  value_vars=["quantity", "final_price"],  var_name="metric",  value_name="value")

#pivot (Long → Wide)
pivot=df.pivot( index="order_id", columns="category", values="final_price")


"""Joins / Merges :

how=  left(keeps all rows from left dataframe...)
      right(keeps  all rows from right dataframe and matching one from letf)
      inner(keeps only matching rows),
      outer(keeps all rows from both datasets)
      cross(all possible combinations)
"""

customers = pd.DataFrame({
    "customer_id": ["C001", "C002", "C003", "C004", "C005", "C006", "C007", "C008"],
    "customer_name": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "segment": ["Retail", "Retail", "Corporate", "Retail", "Corporate", "Retail", "Retail", "Corporate"]
})

merge_1=df.merge(customers, on="customer_id", how="inner")
merge_2=df.merge(customers, on="customer_id", how="left")

#cumulative sales per region
df["cum_sales"] = df.sort_values("order_date").groupby("region")["final_price"].cumsum()


#time based grouping
df.set_index("order_date").groupby( pd.Grouper(freq="M"))["final_price"].sum()





'''
INTERPOLaION--

linear--straight line between two known points
time--works for time series(fill missing data based on time index)
polynomial--fits a polynomial of given order
nearest,spline,pad,quadratic etc
'''
# import pandas as pd
# data={
#     "name":['ramjan','rakib','rafi','raihan','raju'],
#     "age":[32,None,34,None,36],
#     "salary":[30000,None,234444,32422,20000],
#     "performance score":[99,None,77,98,95]
# }
# df=pd.DataFrame(data)
# print('before interpolate')
# print(df)
# print('after interpolate')
# df["age"]=df['age'].interpolate(method='linear')
# print(df)



"""
concatenation:combine datasets vartically(row-wise) or horizontally(column-wise)
pd.concat([df1,df2], axis=0, ignore_index=true)
"""

# df_1=pd.DataFrame({
#     "customerID":[1,2],
#     "name":['rakib','raihan']
# })
# df_2=pd.DataFrame({
#     'customerID':[3,4],
#     'name':['tajrian','pranto']
# })
# df_concate=pd.concat([df_1,df_2], ignore_index=True)  #vertically
# print(df_concate)

# df_concate1=pd.concat([df_1,df_2], axis=1 , ignore_index=True)  #horizontally
# print('horizontally')
# print(df_concate1)