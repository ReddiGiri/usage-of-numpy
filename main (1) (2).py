#create 5*5 array with numbers 1-25,extract the midddle 3*3 matrix block 
import numpy as np
'''arr = np.arange(1,26).reshape(5,5)
print("the array is:\n",arr)
middle_block = arr[1:4, 1:4]
print("middle block:\n",middle_block)'''
#Try broadcasting operation 0f addtion[1,2,3,4] to your own 4*4 matrix
'''A=np.arange(1,17).reshape(4,4)
B=np.array([1,2,3,4])
print("The broadcasting:\n",A+B)'''
#create an array 10 numbers replace all even numbers with -1 
arr = np.arange(1,11)
print("The original array:\n",arr)
arr[arr%2 == 0] = -1 
print("After replacing with even numbers with -1:\n",arr)