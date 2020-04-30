# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 12:54:49 2020

@author: ninjaac
"""


import numpy as np
arr=np.arange(100000)
list=[x for x in range(1,100000)]

#creation odf numpy array
a=np.arange(1,10000,2)
b=np.ones(2)
b2=np.ones_like(a)
c=np.zeros((2,3),order='C')

#_like functio create the array with the same shape and size dtype to the given array
c2=np.zeros_like(b)

d=np.empty((2,3),dtype='int8',order='C')
d2=np.empty_like(c)
e=np.full((2,3),dtype='int8',order='C',fill_value=68)
e2=np.full_like(d,fill_value=10,dtype='float64')
f=np.eye(3)
 
# manupulation of the array
#not like list ans set dict 
# it cane iteratable
# easy to manupulate

#mathamtics +_*/

aa=a+a
bb=b-b

# 10 will multiply through the all elememntd in the array
cc=c*10         
o1=np.array([2,5,3])
oo2=o1/2

o=np.array([2,5,3])
oo=o//2

arr=np.array([[1,2,3],[0,6,7]])
arr1=np.array([[0,4,6],[0,2,8]])
arr>arr1

"""array([[ True, False, False],
       [False,  True, False]])"""

#indexing and slicing 

arr=np.array([
                [1,2,3],
                [0,6,7]
            ])
arr[0][2] #3

#slicing
#2d slicing
arr[:,0] #array([1, 0])

arr[::-1]
#reversing the rows
"""array([[0, 6, 7],
       [1, 2, 3]])"""

# if we changed the sliced array values it will affect the original array
# to avoid that use copy() function 
arr2=arr[:,1:3]
"""array([[2, 3],
       [6, 7]])"""
arr2[0][1]=10
arr2
"""array([[ 2, 10],
       [ 6,  7]])"""
arr 
"""array([[ 1,  2, 10],
       [ 0,  6,  7]])"""

arr2=arr[:,1:3].copy()
"""array([[2, 3],
       [6, 7]])"""
arr2[0][1]=10
arr2
"""array([[ 2, 10],
       [ 6,  7]])"""

# but when we use copy() function it will not affect the original array
arr
"""array([[1, 2, 3],
       [0, 6, 7]])"""