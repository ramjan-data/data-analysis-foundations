#to read a file
import pandas as pd
df=pd.read_excel("pandas\Chapter - 1 - Excel_Data_Analysts_Training (1).xlsx")    #read_csv, read_json
print(df)

# #read multiple sheet from one file
df = pd.read_excel("file.xlsx ",  sheet_name='Sheet2')

#1d file and indexing
#SERIES
s = pd.Series([3, -5, 7, 4],  index=['a',  'b',  'c',  'd'])
print(s)

# custom index
marks = [67,57,89,100] 
subjects = ['maths','english','science','hindi'] 
hdf=pd.Series(marks,index = subjects)
print(hdf)


#append two series in pandas 
# Data to be stored in the Pandas Series
data1 = [10, 20, 40, 80, 100]
data2 = [150, 200]
series1 = pd.Series(data1, index = ["RowA", "RowB", "RowC", "RowD", "RowE"])
series2 = pd.Series(data2, index = ["RowF", "RowG"])
result =pd.concat([series1, series2], ignore_index = False)  #concating
print(result)



ss=pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])
print(ss)


#save new data
data={
    "id" : [1,2,3,4,5],
    "name":["tirtha","ramjan","tajrian","mahadi","hasib"],
    "department" :["software","deployment","DS","machine learning", "DS"],
    "score" :[230,300,435,123,234],
    "salary":[120000,100000,45000,60000,230000]
}

df=pd.DataFrame(data,index=[1,2,3,4,5])
#print(df)

#save as excel and csv and json
df.to_excel("employee.xlsx",index=False ) #we use index=False to avoid default column
df.to_json("employee.json", index=False)

#EXPLORE DATA AS MUCH AS POSSIBLE
#head(n)-->gonna show first n rows
#tail(n)-->last n rows----in both  case n=5 is by default value
dff=pd.read_excel("pandas/Chapter - 1 - Excel_Data_Analysts_Training (1).xlsx") 
print(dff.head(5))  #first 5 rows

print(" ")

print("last 5 rows are")
print(dff.tail(5))  #last 5 row
print(df.head(3))

#info()--method
'''
1.number of column and rows
2.column name
3.data types
4.non null  counts
5.memory usage of  the data frame
'''

print(dff.info())
print(df.info())

# #use describe()
print(f"descriptive statisic\n{df.describe().round(2)}")  #used the round(2) to get only two values after dot
print(f'shape: {df.shape}')  #shape(rows,columns)
print(f'column names: {df.columns}')  #column names
print(df.count())
print(df.dtypes)


'''
1---select specific column--
i.a series, 
ii.dataframe multiple columns of data
column=df["column name"]
subset=df["column1","column2","..."]

2---filter rows--boolean indexing 
filtered_rows=df[df["slary"]>5000]--->one conditions
filtered_rows=df[(df["salary"]>50000) and (df["salary"]<80000)] ---multiple condition
'''

print(f"sample dataframe\n{df}")
print("names from the list")
print(df["name"]) #selecting single column

print(df[["name","score","salary"]])   #selecting multiple columns

"""SELECTING ROWS"""
print(df.iloc[0])       #selecting first rows by position
print(df.iloc[:2])      #selecting first two rows by position
print(df.loc[0])        #selecting  first rows by index 
print(df.loc[0:2, ["name","salary"]])       #slice and specific cols


"""RANKING"""
df["salary_rnk"]=df["salary"].rank()


"""filtering"""
print(df[df["salary"]>100000]) #using one conditions

print(df[(df["score"] > 200) & (df["salary"] >= 100000)])  #use &,| instead of and,or


"""add a new column in dataset"""
df["bonus"]= df["salary"]*0.1  #add bonus 10% of their salary
print(df)
#update salary 5%
df["salary"]=df["salary"]*1.05
print(df)

#use insert() to add new column on special location--->>df.insert(index,"column_name",some_data)
df.insert(4,"bonus", df["salary"]*0.1)
print(df)

#use (df.loc[index, "column name"]=new value) to update a value under column
df.loc[1,"salary"]=70000
df.loc[:3,"salary"]=70000
print(df)


'''removing column'''
df.drop(columns=['performance score'], inplace=True) #remove single column
print(df)

df.drop(columns=["performance score","bonus"], inplace=True) #remove mutiple columns
print(df)

'''use .drop(index) to remove rows'''
df=df.drop(2)  
print(df)

'''SORTING
sorting data 1 column , sort_values()
df.sort_values(by="column name", ascending/descending=true/false, inplace=true/false) ----inplace=true means change the oringinal dataframe'''

df.sort_values(by="age",ascending=True, inplace=True)           #sorting with single column
df.sort_values(by=["age","salary"], ascending=[True,False],inplace=True)          #sorting with multiple columns
print(df)


#aggregation
"""mean(), sum(), min(), max(),  std(), count(), var() etc..."""
print(df["salary"].mean())  #average salary
print(df['salary'].sum())   #sum of all salaries
#so on...



'''handling missing data'''
# 1.detect the missing data with isnull()-- if its True(=missing),False(=not missing)
# 2.handle it(add something or remove)

data1={
    "name":['ramjan',None,'rafi','raihan','raju'],
    "age":[32,None,32,34,22],
    "salary":[30000,None,234444,None,20000],
    "performance score":[99,None,77,98,95]
}
dfa=pd.DataFrame(data1)
print(dfa)
print(dfa.isnull().sum())  #isnull().sum()--total missing value and detect the missing place

#use dropna(axis=0/1, inplace=true) to remove the missing value---->> 0=rows,1=columns
dfa.dropna(axis=1, inplace=True)  #axis=1, removing all column with missing values
print(dfa)

#USE fillna(value, inplace=true) to add some values on missing place
dfa.fillna(0, inplace=True)    #add 0 on all missing places
print(dfa)

dfa["age"].fillna(dfa["age"].mean() , inplace=True)  #add mean value of ages in just age columns missing places
dfa["salary"].fillna(dfa["salary"].median(), inplace=True)   
dfa["name"].fillna("areeba", inplace=True)
print(dfa)


"""handle duplicates"""
print(df.duplicated().sum())      #detect duplicates
print(df.drop_duplicates(keep="first"))  #drop duplicates but keep first occurance
print(df.drop_duplicates(keep="last"))   #keep last occurance
#specific columns
print(df.duplicated(subset=["name"]))
print(df.drop_duplicates(subset=["name"], keep="first"))

"""renaming columns"""
df.rename(columns={"name":"Name", "salary": "Salary"}, inplace=True)

"""changing datatypes"""
df["salary"]=df["salary"].astype("float") #int,string


"""replacing values"""
df["department"].replace({"DS":"data science", "machine learning":"ML"},inplace=True)

"""map,apply,applymap"""
#map only works for single columns
df["status"]=df["score"].map({230:'good',300:"best", 435:"excellent", 123:"bad",234:"good"})
df["score"]=df["score"].map(lambda x: x*2)
#apply
df["score double"]=df["score"].apply(lambda x: x*2)
df["total"]=df.apply(lambda row : row["score"]+ row["score double"], axis=1)  
col_max=df.apply(lambda col: col.max(), axis=0)  #find max values of each columns
print(col_max)
df_squared=df.applymap( lambda x: x**2)  #it square every cell in datasets





"""stacking and unstacking"""
stacked=df.set_index("name").stack()
print(stacked)
unstacked=stacked.unstack()
print(unstacked)



"""pivot and pivot tables"""
df=pd.DataFrame({"name":["alice","alice","bob","bob"],
                 "subjects":["math","math","science","science"],
                 "score":[87,67,87,89]
                 })
print(df)
pivoted=df.pivot(index="name",columns="subjects", values="score")
print(pivoted)
pivot_tbl=pd.pivot_table(df, index="name", columns="subjects", values="score", aggfunc="mean")
print(pivot_tbl)





'''
INTERPOLaION--

linear--straight line between two known points
time--works for time series(fill missing data based on time index)
polynomial--fits a polynomial of given order
nearest,spline,pad,quadratic etc
'''
import pandas as pd
data={
    "name":['ramjan','rakib','rafi','raihan','raju'],
    "age":[32,None,34,None,36],
    "salary":[30000,None,234444,32422,20000],
    "performance score":[99,None,77,98,95]
}
df=pd.DataFrame(data)
print('before interpolate')
print(df)
print('after interpolate')
df["age"]=df['age'].interpolate(method='linear')
print(df)


"""GROUPING"""
data={
    "name":['ramjan','rakib','rafi','raihan','raju'],
    "age":[32,26,34,32,36],
    "salary":[300000,234900,234444,332422,20000],
    "performance score":[99,23,77,98,95]
}
df=pd.DataFrame(data)
grouped=df.groupby("age")["salary"].sum()  #single column
m_grp=df.groupby(["age","name"])["salary"].sum()  #multiple columns
print(grouped)
print(m_grp)




'''MERGING
how=left(keeps all rows from left dataframe...)
      =right(keeps  all rows from right dataframe and matching one from letf)
      inner(keeps only matching rows),
      outer(keeps all rows from both datasets)
      cross(all possible combinations)
'''
data1={
    "name":['ramjan','rakib','rafi','raihan','raju'],
    "age":[32,26,34,32,36],
    "salary":[300000,234900,234444,332422,20000],
    "performance score":[99,23,77,98,95]
}
df=pd.DataFrame(data1)
data2={
    "name":['ramjan','rakib','rafi','raihan','raju'],
    "age":[32,31,32,34,22],
    "salary":[30000,50000,234444,32422,20000],
    "performance score":[99,89,77,98,95]
}
dff=pd.DataFrame(data2)
marge=pd.merge(df, dff, on="performance score" ,how="inner")  #how=left,cross,right,inner,outer




"""
concatenation:combine datasets vartically(row-wise) or horizontally(column-wise)
pd.concat([df1,df2], axis=0, ignore_index=true)
"""

df_1=pd.DataFrame({
    "customerID":[1,2],
    "name":['rakib','raihan']
})
df_2=pd.DataFrame({
    'customerID':[3,4],
    'name':['tajrian','pranto']
})
df_concate=pd.concat([df_1,df_2], ignore_index=True)  #vertically
print(df_concate)

df_concate1=pd.concat([df_1,df_2], axis=1 , ignore_index=True)  #horizontally
print('horizontally')
print(df_concate1)





"""string operation"""
data2={
    "name":['ramjan','rakib','rafi','raihan','raju'],
    "age":[32,31,32,34,22],
    "salary":[30000,50000,234444,32422,20000],
    "performance score":[99,89,77,98,95]
}
dff=pd.DataFrame(data2)
print(dff["name"].str.upper())  #ALL CAPITAL
print(dff["name"].str.lower())  #all small
print(dff["name"].str.title())   #first letter capital
print(dff["name"].str.len())
print(dff["name"].str.replace("ra","RA"))   #replace ra to RA\


