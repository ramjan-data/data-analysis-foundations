import numpy as np
import pandas as pd

"""Data structure : 
                a. Series
                b.DataFrame
"""

#Series(1D)
s=pd.Series([10,20,30,40], index=['a',  'b', 'c', 'd'])
print(s)


#append two series in pandas 
# Data to be stored in the Pandas Series
data1 = [10, 20, 40, 80, 100]
data2 = [150, 200]
series1 = pd.Series(data1, index = ["RowA", "RowB", "RowC", "RowD", "RowE"])
series2 = pd.Series(data2, index = ["RowF", "RowG"])
result =pd.concat([series1, series2], ignore_index = False)  #concating
print(result)

#DataFrame
df=pd.DataFrame({
    'name' : np.random.choice(['ramjan', 'tirtha', 'tajrian'], size=100),
    'age': np.random.randint(20,25,100),
    'salary' : np.random.uniform(30000, 50000, 100)
})
print(df.head())




"""Reading Data
        example:csv  -pd.read_csv("data.csv")
                excel-pd.read_excel("file.xlsx", sheet_name="Sheet1")
                sql  -pd.read_sql(query, connection)...

        to write data:  
                    -df.to_excel("employee.xlsx",index=False )
                    -df.to_csv("file name.csv")...
"""
#to read
exc=pd.read_excel(r"C:\Users\USER\OneDrive\Desktop\python\pandas\Chapter - 1 - Excel_Data_Analysts_Training (1).xlsx")
print(exc.head())

csv=pd.read_csv(r"C:\Users\USER\OneDrive\Desktop\python\pandas\heyyy.csv")
print(csv.head())

# to write
df.to_excel("employee.xlsx",index=False ) #we use index=False to avoid default column
df.to_json("employee.json", index=False)



#First Things You MUST Do After Loading Data
df.head()            
df.tail(10)  #it will show the last  10 rows
df.shape             
df.info()            
df.describe()   
df.dtypes
df.count()

#to change data type 
df["name"] = df["name"].astype("category")



"""Column selection"""
#sinle column
df["age"]

#multiple column
df[["age", "salary"]]



"""copy vs view"""
#view : This causes silent bugs
df2 = df[["age", "salary"]]
df2["age"] = 100  # warning
print(df2)

#copy--always go with this
df2 = df[["age", "salary"]].copy()
df2["age"] = 100
print(df2)




"""Basic filtering: Use- & / | """
#single condition
df[df["age"] > 25]

#multiple condition
df[(df["age"] > 25) & (df["salary"] > 40000)]




"""Sorting and Renaming and Ranking"""

df=df.sort_values(by="salary", ascending=False)
df=df.sort_values(by=["age","salary"], ascending=[True,False])

df=df.rename(columns={"salary": "monthly_salary"})

df["age_rank"] = df["age"].rank(ascending=False)
print(df)

