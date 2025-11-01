#start
import numpy as np
prices=np.array([100,200,300])
discount=10
final_prices=prices-(prices*discount/100)
print(final_prices)

arr=np.array([100,200,300])
print(arr*2)



#missing and special value
arr=np.array([1,2,np.nan,4,np.nan,6])
print(np.isnan(arr))

#replace nan numbers
#np.nan_to_num(array,nan=value),default-0
arr=np.array([1,2,np.nan,4,np.nan,6])
cleaned_arr=np.nan_to_num(arr)
nn=np.nan_to_num(arr,nan=100)
print(cleaned_arr)
print(nn)

#infinite number----np.isinf(array)
arr=np.array([1,2,np.inf,4,-np.inf,6])
print(np.isinf(arr))
cleaned_arr=np.nan_to_num(arr,posinf=1000,neginf=-1000)
print(cleaned_arr)







#np.insert(array,index,value,axis)
import numpy as np
arr=np.array([10,20,30,50,40,60])
new_arr=np.insert(arr,2,100,axis=0) #axis is optional for 1d
print(new_arr)

arr_2d=np.array([[2,3],
                 [4,9]])
new_arr_2d=np.insert(arr_2d,1,[5,6],axis=0) #insert a new row at index 1
print(new_arr_2d)

#np.append()
arr=np.array([10,20,30,50,40,60])
new_arr1=np.append(arr,[40,50,90])  #[10,20,30,50,40,60,40,50,90]
print(new_arr1)

#concate-----np.concatenate((array1,array2),axis=0)---axis=0-->varticle stalking,axis=1-->horizontal stalking
arr1=np.array([10,20,60])
arr2=np.array([30,40,90])
new_arr=np.concatenate((arr1,arr2))
print(new_arr)

#removing element of array--->np.delete(array,index,axis=none)
arr=np.array([10,20,30,50,40,60])
new_arr=np.delete(arr,0)
print(new_arr)   #[20 30 50 40 60]
#for 2d array
arr=np.array([[1,2,3],[4,5,6]])
new1=np.delete(arr,0,axis=0)   #[[4,5,6]]
new2=np.delete(arr,1,axis=0)   #[[1,2,3]]
print(new1)
print(new2)

arr = np.array([10,20,30,40])
ar=np.delete(arr, [1,3])        # [10 30]


#stacking--->vstack()row  wise,hstack()colunm wise
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
print(np.vstack((arr1,arr2)))
print(np.hstack((arr1,arr2)))

#splitting-->np.split()-equal,np.hsplit(),np.vsplit()
arr=np.array([10,20,30,40,60,55])
print(np.split(arr,2))

