import matplotlib.pyplot as plt
import numpy as np

x=[1,2,3,4]
y=[10,30,20,15]
plt.plot(x,y)
#plt.show()


"""object oriented api"""
a=["sat","sun","mon","tues","wed","thurs"]  #x-axis data
b=[10,17,7,18,20,13]
fig,ax=plt.subplots()
ax.plot(a,b)
ax.set_title("bakery sales this weeks")
ax.set_xlabel("day of the week")
ax.set_ylabel("sales per day")
plt.show()


#ax.plot(x,y, color="color name", linestyle="line_style", linewidht="value", marker="marker symbol", markersize/ms=float, markeredgecolor/mec='color', label= "label name", alpha=0.8)
a=["sat","sun","mon","tues","wed","thurs"]  #x-axis data
b=[10,17,7,18,20,13]
fig1,ax=plt.subplots()
ax.plot(a,b, color="green", linestyle="--", linewidth=3, marker="o", label="daily sales")
ax.set_title("bakery sales this week")
ax.set_xlabel("day of the week")
ax.set_ylabel("sales per day")
ax.legend()                #ax.legend(loc='upper left', frontsize=12)
ax.grid(True, color="gray", linestyle=":", linewidth="0.5")  #ax.grid(axis="x")- vertical line, axis='y'-horizontal line

"""if we want to controll the limits of data"""
#ax.set_xlim(0,6)  
ax.set_ylim(0,30)   #(min, max)

""" replacing the data"""
ax.set_xticks(["sat","sun","mon","tues","wed","thurs"],["saterday","sunday","monday","tuesday","wednesday","thursday"])
plt.show()




"""BASIC Plotting"""
# ax.plot()  --line plot 
# ax.scatter() 
# ax.bar()
# ax.barh()  -horizontal bar 
# ax.hist(data, bins=10,...)  --histogram
# ax.boxplot(data)   
# ax.pie([10,7,4], labels=['dhaka','ctg','cumilla'], autopct='%1.1f%%, colors=['gold','green','red'])


#pie chart
regions=['dhaka','ctg','cumilla','sylhet','barisal']
revenue=[180,100,32,40,80]
fig2,p=plt.subplots()
p.pie(revenue, labels=regions, autopct="%1.1f%%", colors=['gold','black','blue','purple','pink'])
p.set_title('revenue contributions  by regions')
plt.show()



#histogram
#.hist(data, bins=numbers_of_bins, color='color name', edgecolor='black)
scores=[45,34,59,89,76,57,54,78,67,46,98,65,67,54]
bines=[0,20,40,60,80,100,120]
fig3, hst=plt.subplots()
#hst.hist(scores, bins=5, color='purple',edgecolor='black')
hst.hist(scores, bins=bines, kde=True, color='purple',edgecolor='black')
hst.set_xlabel('score range')
hst.set_ylabel('numbers of students')
hst.set_title('score distribution of student')
plt.show()




#scatter diagram(to find relations between two variables)
#.scatter(x,y, color='color name', marker='marker style', label='label name')
study_hr=[3,4,5,6,7,8,9,10]
marks=[77,87,37,67,89,88,96,99]
fig4, sc=plt.subplots()
sc.scatter(study_hr,marks, color='pink', marker='o', label='CLASS A')
sc.scatter([3,4,5,6,7,8,9,10],[77,79,83,85,88,92,95,98], color='blue', marker='o' , label='CLASS B')
sc.set_xlabel('Study hours per day')
sc.set_ylabel('Marks of the students')
#sc.set_title('relationship between study time and exam score')
sc.set_title("comparison between two class")
sc.legend()
sc.grid(True)
plt.show()




#subplots
#fig, ax=plt.subplots(nrows, ncols, figsize=(width, height))
fig5, bx=plt.subplots(1,2, figsize=(10,5))
x=[1,2,3,4]
y=[10,20,15,8]
bx[0].plot(x,y)
bx[0].set_title("line grap")

bx[1].bar(x,y)
bx[1].set_title('bar chart')
fig5.suptitle("comparison of line and bar chart")
plt.tight_layout() #avoid overlap
plt.show()



'''if-- fig, bx=plt.subplots(2,2, figsize=(10,5))
bx[0,0]-top left
bx[0,1]-top right
bx[1,0]-bottom left
bx[1,1]-bottom right '''





#save those all figures(savefig())
#savefig('filename.extention', dpi=value, bbox_inches='tight')
fig1.savefig('line graph.png',dpi=300, bbox_inches='tight')
fig2.savefig('pie chart.pdf', dpi=300, bbox_inches='tight')
fig3.savefig('histogram.jpg', dpi=300, bbox_inches='tight')
fig4.savefig('scatter.png',   dpi=300, bbox_inches='tight')
fig5.savefig('subplots.png',  dpi=300, bbox_inches='tight')




"""SOME OTHER PLOTS"""

#box plot
data = np.random.normal(50, 15, 200)
plt.boxplot(data)
plt.title("Box Plot Example")
plt.show()

#violinplot
data = [np.random.randint(1,100,50)]
plt.violinplot(data, showmedians=True)
plt.title("Violin Plot Example")
plt.show()


#area plot(fill between)
x = [1,2,3,4,5]
y = [1,4,6,8,10]

plt.fill_between(x, y, color="orange", alpha=0.4)
plt.plot(x, y, color="red")
plt.title("Area Plot Example")
plt.show()


#stem plot
x = [1,2,3,4,5]
y = [2,4,6,8,10]

plt.stem(x, y)
plt.title("Stem Plot Example")
plt.show()
