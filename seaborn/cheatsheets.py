import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_excel("supermarket_sales.xlsx")
print(df)
print(df.info())

sns.get_dataset_names()
titanic=sns.load_dataset('titanic')



#COUNT PLOT
#countplot(x='variable', y='', hue=another variable, data=dataset, order=[], hue_order=[], color='', palette='color',linewidth='')
#sns.countplot(x='Gender', hue='Branch', data=df)

fig1, ax=plt.subplots(figsize=(12,5))
sns.countplot(y='Product line', hue='Gender', data=df, palette='gist_gray', ax=ax)
ax.set_title("product line of a supermarket sales")
#ax.set_xlabel("product line")
ax.set_ylabel("count for each")
plt.show()



#BAR PLOT
fig2, bx=plt.subplots(figsize=(13,6))
sns.barplot(x='Product line',y='Total',  hue='Gender', data=df, ax=bx ,color='gray', capsize=0.2, ci=None) #also estimtor=sum/np.median...
plt.show()



#BOX PLOT
#boxplot(x,y,hue,data,order,hue_order,color,palette,width=0.8(#box width), fliersize=5(#outliers))
fig3, cx=plt.subplots(figsize=(12,5))
sns.boxplot(x='Payment', y='Total', hue='Gender', data=df, ax=cx, width=0.7,fliersize=5, showmeans=True, meanprops={'marker':'o','markersize':'8','markerfacecolor':'white'})
plt.show()
#make a boxplot for all numeric columns
plt.figure(figsize=(12,6))
sns.boxplot(data=df)
plt.show()



#VIOLIN PLOT
#violinplot(..., bw=o.2, cut=3, scale='area',inner='box',linewidth=1...)
fig4, dx=plt.subplots(figsize=(12,6))
sns.violinplot(x='Payment',y='Total', hue='Gender', hue_order=['Male','Female'], data=df, ax=dx, inner='box', bw=.2,cut=2) #inner=box/stick/quartile
plt.show()



#STRIP PLOT
#stripplot(jitter=true, dodge=false,alpha=0.8...)
fig5,ex=plt.subplots(figsize=(12,6))
sns.stripplot(x='Payment',y='Total', hue='Gender', ax=ex, data=df, jitter=True, dodge=False, alpha=0.9)
plt.show()



#swarm plot(similar to strip plot. if dataset is small then use it otherwise strip plot)
fig6,fx=plt.subplots(figsize=(12,6))
sns.swarmplot(x='Payment',y='Total', hue='Gender', ax=fx, data=df, alpha=0.9)
plt.show()




#cat plot
sns.catplot(data=df, x='Payment',y='Total', col='Gender', kind='swarm',row='Customer type')
plt.show()




#histogram
sns.histplot(data=df, x='Total', bins=np.arange(0,1100,50), kde=True, element='bars', hue='Gender')
plt.show()



#kde plot
sns.kdeplot(data=df, x='Total', hue='Payment', multiple='stack', palette='gist_gray', linewidth=0.5, )
plt.show()



#rug plot
plt.figure(figsize=(12,5))
sns.scatterplot(data=df, x='Unit price',y='gross income', hue='Gender')
sns.rugplot(data=df, x='Unit price',y='gross income', hue='Gender', height=-0.04)
plt.show()



#ECDF
sns.ecdfplot(data=df, x='gross income',hue='Gender',stat='proportion')
plt.show()



#displot
sns.displot(data=df, x='Total', kde=True) #histogram+kde
sns.displot(data=df, x='Total', y='gross income', kind='kde')
plt.show()



#joint plot(to find relation between two variables)
sns.jointplot(data=df, x='Total', y='gross income', kind='hex')   #hexabin plot
plt.show()



#scatterplot
sns.scatterplot(data=df, x='Total', y='gross income', hue='Gender', palette='gist_gray')
plt.show()


#pair plot
sns.pairplot(data=df,x_vars=['gross income','Total','Tax 5%'],y_vars=['gross income','Unit price','gross margin percentage'], kind='scatter', diag_kind='kde', hue='Gender', palette='gist_gray', corner=True)



#line plot
sns.lineplot(data=df, x='Total',y='gross income')
plt.show()



#rel plot
sns.relplot(data=df, x='Total', y='Payment', hue='Gender', kind='scatter')
plt.show()



#regression plot
sns.regplot(data=df,x='Total', y='gross income',color='gray', line_kws=dict(color='red',linestyle='--'))
plt.show()



#heat map
dff=pd.read_excel("mart_linePlot.xlsx")
dff.columns=dff.columns.str.lower()
#print(dff.head(2))
dffpiv=dff.pivot_table(index='outlet_year',columns='outlet_size',values='sales')
#print(dffpiv)



sns.set_style('white')
sns.heatmap(data=dffpiv,annot=True, fmt='.0f',annot_kws=dict(size=15, weight='bold'))
plt.show()


