import pandas as pd
import datetime as dt
#converting text into datetime
date='2025-09-17'
df=pd.to_datetime(date)
print(df)

dates = ['2025-09-17', '17/09/2025', 'Sep 17 2025']

dff=pd.to_datetime(dates, errors="coerce")
print(dff)

drange=pd.date_range(start='2025-01-01', end='2025-01-10', freq='2D')  #D,H,M(month end),MS(month start),W,Y,B(monday-friday only),
print(drange)


df1 = pd.DataFrame({
    'date': pd.date_range('2025-01-01', periods=5, freq='D'),
    'value': [10, 20, 30, 40, 50]
})
'''datetime as index'''
df1['date'] = pd.to_datetime(df1['date'])
df1.set_index('date', inplace=True)
print(df1)

#accessing date parts
df1['year']=df1['date'].dt.year
print(df1['year'])   #month,day,hour,minute,.second,day_name, month_name,isocalendar(week numbers)


#timedelta
now = pd.Timestamp('2025-09-17')
past = pd.Timestamp('2025-09-10')
diff = now - past
print(diff.days)           # 7

#resampling
df1.set_index('date', inplace=True)
res=df1.resample('M').sum()
mres=df1.resample('M').agg({'value' : ['sum','mean','max']})  #multiple statistics values at once
print(res)
print(mres)

#rolling window values
df['7d_avg'] = df['value'].rolling(window=7).mean()
print(df['7d_avg'])


"""localizing timezone"""
df.index = df.index.tz_localize('UTC')
df.index = df.index.tz_convert('Asia/Dhaka')
print(df)

#fillna 
# Fill missing values
df['value'].fillna(method='ffill', inplace=True)  # forward fill
# or df['value'].fillna(0)


"""CATEGORICAL"""
df=pd.Series(['male','female','male','female','others'])
cat_data=df.astype("category")
print(cat_data)

'''working with categories'''
print(cat_data.cat.categories)  #checking unique categories
cat_data=cat_data.cat.rename_categories({'male':'M','female':'F', 'others':'O'})   #renaming the categories
cat_data=cat_data.cat.add_categories(['unknown'])                 #add new category
cat_data=cat_data.cat.remove_categories(['O'])                    #remove category


'''oredered categorical data'''
grades=pd.Series(['A','D','C','A','B','A','C'])
grades=grades.astype(pd.api.types.CategoricalDtype(categories=['A','B','C','D'], ordered=True))
print(grades)
print(grades.min(),grades.max())

