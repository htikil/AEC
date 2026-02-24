import numpy as np
   
a=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])

b=np.array([[1,2,3],
            [4,5,6],
            [7,8,9]])

print(a)

reshape_a = a.reshape(1,9)
print(reshape_a)

ar=np.array([1,2,3])
br=np.array([5,6,7])
product = ar*br
print(product)