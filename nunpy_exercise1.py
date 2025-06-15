import numpy as np

array1 = np.array([1,5,4,14])


num = array1[2] + array1[0]

print(" this is sum : " , num)

print(type(array1))
print(np.__version__)




a = np.array(42)
b = np.array([-1,0,3,4])
c = np.array([[4,5,6],[7,8,9]])
d = np.array([[[4,5,6],[1,2,3]],[[1,2,3,],[4,5,6]]])



fruit =np.array (['apple','orange', 'banana' ])


floatarr= np.array([20.2,15.4 ,40.5,45.2])





print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)



arr = np.array([4,10,1,15,24,56,58] , ndmin=5 )
print(arr)
print (arr , "and  ndim ", arr.ndim)

print  ("s array 1 line 2 nd elemt is" , c[0,1]) # 5 
print  ("s array 2  line 2 nd elemt is" , c[1,1]) # 8



print( b [:1]) # print :1 before indexes 
print( b[1:]) # print 1: after indexes
 
print (b [0:2]) #range index
print (b[0:4:2] ) # start 0 ,end point 4,skip 2  

# data type 
print (c.dtype)
print(fruit.dtype)  
# converting data typpe

print (floatarr)
newar = (floatarr.astype ('i'))
print (newar)

newar1 =(b.astype('bool'))
print(newar1)


arrc = np.array([4,5,10,25])
x = arrc.copy()
arrc[0] = 42

print(arrc)
print(x)


y = arrc.view()
print(y)



arrf =np.array ([1,2,3])

arrs = np.array([4,5,6])

arrt = np.array([7,8,9])

arrcon = np.concatenate((arrf,arrs)) #cocatenete

arrstack = np.stack((arrf,arrs),axis=1 )

print("array stack " ,arrstack)


print("concatenate : ",arrcon)