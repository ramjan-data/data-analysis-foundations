import pandas as pd
df=pd.read_csv(r"C:\Users\USER\OneDrive\Desktop\python\sales_orders.csv")
print(df.head())



"""loc vs iloc :
                loc → label-based
                iloc → position-based
                
                
                """
print(df.loc[0])       # label 0 (if index is default)
print(df.iloc[0])      # first row

#select rows + columns
print(df.loc[0:3, ["order_id", "region", "product"]])
print(df.iloc[0:3, 0:4])



"""Setting and  Resetting index"""
df = df.set_index("order_id")
df = df.reset_index()



"""Conditional Selection (Advanced Filtering)"""
df[
    (df["region"] == "Asia") &
    (df["category"] == "Electronics") &
    (df["quantity"] >= 1)
]

#using isin
df[df['region'].isin([' Asia', 'Europe'])]



#Assignment-create new column
df["total_price"] = df["quantity"] * df["unit_price"]

#Assignment-Discount handling
df["discount"] = df["discount"].fillna(0)
df["final_price"] = df["total_price"] * (1 - df["discount"])

#Assignment : profit calculate
df["profit"] = df["final_price"] * 0.2



"""Missing Data"""
#detect
df.isna().sum()

#Drop--dropna(axis=0/1) to remove the missing value---->> 0=rows,1=columns
df=df.dropna(axis=1)  #axis=1, removing all column with missing values
print(df)

#USE fillna(value, inplace=true) to add some values on missing place
df=df.fillna(0)    #add 0 on all missing places
print(df)

df['age']=df["age"].fillna(df["age"].mean()) 
df['salary']=df["salary"].fillna(df["salary"].median(), inplace=True)   
df["name"]= df["name"].fillna("areeba", inplace=True)
print(df)

#Forward / backward fill
df=df.fillna(method="ffill")
df=df.fillna(method="bfill")



"""handle duplicates"""
print(df.duplicated().sum())      #detect duplicates
df=df.drop_duplicates(keep="first")  #drop duplicates but keep first occurance
df=df.drop_duplicates(keep="last")  #keep last occurance
#specific columns
df=df.duplicated(subset=["order_id"])
df=df.drop_duplicates(subset=["order_id"], keep="first")



"""Type Conversion"""
#check
df.dtype

#fix
df["returned"] = df["returned"].astype('bool')
df["region"] = df["region"].astype("category")

#DateTime
df["order_month"] = df["order_date"].dt.month
df["order_year"] = df["order_date"].dt.year



"""String Operations"""
df["product"] = df["product"].str.lower()
df["product"].str.contains("phone")
df["region"].str.strip()
# print(dff["col"].str.upper())  #ALL CAPITAL
# print(dff["col"].str.lower())  #all small
# print(dff["col"].str.title())   #first letter capital
# print(dff["col"].str.len())
# print(dff["col"].str.replace("ra","RA"))   #replace ra to RA\





"""Inserting columns"""
#use insert() to add new column on special location--->>df.insert(index,"column_name",some_data)
df.insert(5, 'tips', df['final_price']*0.01)


#use (df.loc[index, "column name"]=new value) to update a value under column
df.loc[1,"salary"]=70000
df.loc[:3,"salary"]=70000
print(df)




'''removing column'''
df=df.drop(columns=['final_price']) #remove single column
print(df)


df=df.drop(columns=["final_price","tips"]) #remove mutiple columns
print(df)

'''use .drop(index) to remove rows'''
# df=df.drop(2)  
# print(df)


"""replacing values"""
#df["department"].replace({"DS":"data science", "machine learning":"ML"},inplace=True)



"""map,apply,applymap"""
#map only works for single columns
# df["status"]=df["score"].map({230:'good',300:"best", 435:"excellent", 123:"bad",234:"good"})
# df["score"]=df["score"].map(lambda x: x*2)
##apply
# df["score double"]=df["score"].apply(lambda x: x*2)
# df["total"]=df.apply(lambda row : row["score"]+ row["score double"], axis=1)  
# col_max=df.apply(lambda col: col.max(), axis=0)  #find max values of each columns
# print(col_max)
# df_squared=df.applymap( lambda x: x**2)  #it square every cell in datasets



