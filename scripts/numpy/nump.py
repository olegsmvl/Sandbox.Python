import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
b = a.sum(axis=0)
print(b)
c = np.array([10,20,30])
print("a+c:\n",a+c)