# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'

#%% [markdown]
#
# HW Numpy 
# ## By: xxx
# ### Date: xxxxxxx
#


#%%
# NumPy

import numpy as np

# %%
# ######  QUESTION 1      QUESTION 1      QUESTION 1   ##########
# This exercise is to test true/shallow copies, and related concepts. 
# ----------------------------------------------------------------
# 
# ######  Part 1a      Part 1a      Part 1a   ##########
# 
list2 = [ [11,12,13], [21,22,23], [31,32,33], [41,42,43] ] # two dimensional list (2-D array)  # (4,3)
nparray2 = np.array(list2)
print("nparray2:", nparray2)
# For details on indices function, see class notes or Class05_02_NumpyCont.py
idlabels = np.indices( (4,3) ) 
print("idlabels:", idlabels)

i,j = idlabels # idlabels is a tuple of length 2. We'll call those i and j
nparray2b = 10*i+j+11
print("nparray2b:",nparray2b)

# 1.a) Is nparray2 and nparray2b the "same"? Use the logical "==" test and the "is" test. 
# Write your codes, 
# and describe what you find.


print(nparray2 == nparray2b)

nparray2 is nparray2b

nparray2 is nparray2 

# we see that even though the values are the same, as we can see in the '==' operator (which compares the contects of each variable), and returns 'True'. 
# Using the 'is' operator returns false. This is becuase the two arrays are two separate objects. They take up different spaces in object memory. The 'is' operator checks their object memory. 


# %%
# ######  Part 1b      Part 1b      Part 1b   ##########
# 
# 1.b) What kind of object is i, j, and idlabels? Their shapes? Data types? Strides? 
# See the lecture 4 notes for reference.
# write your codes here
#

#Object 


# The shape of each variable
print(f" i shape: {i.shape}")
print(f" j shape: {j.shape}")
print(f" idlabels shape: {idlabels.shape}")

# The Stride of each variable

print(f"Stride of i: {i.strides}")
print(f"Stride of j: {j.strides}")
print(f"Stride of idlabels: {idlabels.strides}")

# Data Type 
print(f"Data type of i: {i.dtype}")
print(f"Data type of j: {j.dtype}")
print(f"Data type of idlabels: {idlabels.dtype}")

# %%
# ######  Part 1c      Part 1c      Part 1c   ##########
# 
# 1.c) If you change the value of i[0,0] to, say 8, print out the values for i and idlabels, both 
# before and after the change.
# 
# write your codes here
# Describe what you find. Is that what you expect?
#
print(i[0,0])
print(idlabels[0,0])

i[0,0] = 8
print(i)
print(idlabels)

# Also try to change i[0] = 8. Print out the i and idlabels again.
i[0] = 8
print(i[0,0])
print(idlabels[0,0])
print(i)
print(idlabels)

# yes, you can see that by changing at exactly the first position nd the first element in that position (ie [0,0]),
# it will only change the first element. when you change the values at the first element (ie [0]) it will change the entire first array. 
# what way surprising is that it will also change the value of idlabels, but it makes sense because
#  i,j = idlabels; what i didn't consider was that idlabels is a list of lists, so when changing i, i am also changing the original list
# if i wanted to avoid this, i would make a shallow copy of the orignal list. 






# %%
# ######  Part 1d      Part 1d      Part 1d   ##########
# 
# 1.d) Let us focus on nparray2 now. (It has the same values as nparray2b.) 
# Make a shallow copy nparray2 as nparray2c
import copy
nparray2c = copy.copy(nparray2)
print(nparray2c)


# now change nparray2c 1,1 position to 0. Check nparray2 and nparray2c again. 
nparray2c[1,1] = 0
print(nparray2c)
print(nparray2)

# Print out the two arrays now. Is that what you expect?
# 
# Yes, this is expected because as we saw above, the lists are mutable, so by making a shallow copy, 
# we no longer are changing the original list. 

# Also use the "==" operator and "is" operator to test the 2 arrays. 
# write your codes here

print(nparray2 == nparray2c)

nparray2 is nparray2c

# as we expect; the value change is different than that of the orignal; and since its a different object, it is also not 
# going to return 'true'



#%%
# ######  Part 1e      Part 1e      Part 1e   ##########
# Let us try again this time using the intrinsic .copy() function of numpy array objects. 
nparray2 = np.array(list2) # reset the values. list2 was never changed.
nparray2c = nparray2.copy() 


# now change nparray2c 0,2 position value to -1. Check nparray2 and nparray2c again.
# Are they true copies?

nparray2c[0,2] = -1
print(nparray2c)
print(nparray2)


#This is a true copy since this is a deep copy. If i were to change the orignal(ie nparray2) it would not change the copy as we see below.

#nparray2[0,0] = 2
#print(nparray2c)

#after running this, go back and rerun the beginning to rest the values, then run the code above it and omit this code to continue
# write your codes here
# Again use the "==" operator and "is" operator to test the 2 arrays. 
print(nparray2c == nparray2)

nparray2c is nparray2

# Here we can see where the value is different and that these are two different objects taking up different spaces


#
# Since numpy can only have an array with all values of the same type, we usually 
# do not need to worry about deep levels copying. 
# 
# ######  END of QUESTION 1    ###   END of QUESTION 1   ##########




# %%
# ######  QUESTION 2      QUESTION 2      QUESTION 2   ##########
# Write NumPy code to test if two arrays are element-wise equal
# within a (standard) tolerance.
# between the pairs of arrays/lists: [1e10,1e-7] and [1.00001e10,1e-8]
# between the pairs of arrays/lists: [1e10,1e-8] and [1.00001e10,1e-9]
# between the pairs of arrays/lists: [1e10,1e-8] and [1.0001e10,1e-9]
# Try to google what function to use to test numpy arrays within a tolerance.
a = np.array([1e10,1e-7])
b = np.array([1.00001e10,1e-8])

result = np.allclose(a, b)
print(result)

#returns False

tolerance = np.max(np.abs(a - b))
print(tolerance)

result = np.allclose(a, b, atol = tolerance)
print(result)

#returns tru because we made the tolerance the lenght of the max absolute vlae between the two

c = np.array([1e10,1e-8])
d = np.array([1.00001e10,1e-9])

result2 = np.allclose(c, d)
print(result2)

#Retuns True; they are the same distance

e = np.array([1e10,1e-8])
f = np.array([1.0001e10,1e-9])

result3 = np.allclose(e, f)
print(result3)

# Returns false, they're not the same distance
tolerance2 = np.max(np.abs(e - f))
print(tolerance2)

result3 = np.allclose(e, f, atol = tolerance2)
print(result3)
# they are the same distance. 

# ######  END of QUESTION 2    ###   END of QUESTION 2   ##########


# %%
# ######  QUESTION 3      QUESTION 3      QUESTION 3   ##########
# Write NumPy code to reverse (flip) an array (first element becomes last).
x = np.arange(12, 38)


reversed_arr = x[::-1]
print(reversed_arr)



# ######  END of QUESTION 3    ###   END of QUESTION 3   ##########


# %%
# ######  QUESTION 4      QUESTION 4      QUESTION 4   ##########
# First write NumPy code to create an 7x7 array with ones.
# Then change all the "inside" ones to zeros. (Leave the first 
# and last rows untouched, for all other rows, the first and last 
# values untouched.) 
# This way, when the array is finalized and printe out, it looks like 
# a square boundary with ones, and all zeros inside. 
# ----------------------------------------------------------------
x = np.full((7, 7), 1) 

#print(x)

for i in range(len(x)):
    for j in range(1,len(x)-1):
        x[i,j]= 0 


print(x)


# ######  END of QUESTION 4    ###   END of QUESTION 4   ##########



# %%
# ######  QUESTION 5      QUESTION 5      QUESTION 5   ##########
# Broadcasting (https://numpy.org/doc/stable/user/basics.broadcasting.html),
# Boolean arrays and Boolean indexing.
# ----------------------------------------------------------------
i=3642
myarray = np.arange(i,i+6*11).reshape(6,11)
print(myarray)
# 
# a) Obtain a boolean matrix of the same dimension, indicating if 
# the value is divisible by 7. 



for i in range(0,len(myarray)):
    for j in range (0, 11):
        if myarray[i,j] % 7 == 0:
            myarray[i,j] = True
        else:
            myarray[i,j] = False
print(myarray)



# b) Next get the list/array of those values of multiples of 7 in that original array  

i=3642
myarray = np.arange(i,i+6*11).reshape(6,11)

arr = []

for i in range(0, len(myarray)):
    for j in range (0,11):
        if myarray[i,j] % 7 == 0:
            arr = myarray[i,j]
            print(arr)


# ######  END of QUESTION 5    ###   END of QUESTION 5   ##########





#
# The following exercises are  
# from https://www.machinelearningplus.com/python/101-numpy-exercises-python/ 
# and https://www.w3resource.com/python-exercises/numpy/index-array.php
# Complete the following tasks
# 

# ######  QUESTION 6      QUESTION 6      QUESTION 6   ##########

#%%
flatlist = list(range(1,25))
print(flatlist) 

#%%
# 6.1) create a numpy array from flatlist, call it nparray1. What is the shape of nparray1?
# remember to print the result
#
# write your codes here
#

#%%
# 6.2) reshape nparray1 into a 3x8 numpy array, call it nparray2
# remember to print the result
#
# write your codes here
#

#%%
# 6.3) swap columns 0 and 2 of nparray2, and call it nparray3
# remember to print the result
#
# write your codes here
#

#%%
# 6.4) swap rows 0 and 1 of nparray3, and call it nparray4
# remember to print the result
#
# write your codes here
#

#%%
# 6.5) reshape nparray4 into a 2x3x4 numpy array, call it nparray3D
# remember to print the result
#
# write your codes here
#

#%%
# 6.6) from nparray3D, create a numpy array with boolean values True/False, whether 
# the value is a multiple of three. Call this nparray5
# remember to print the result
# 
# write your codes here
#

#%%
# 6.7) from nparray5 and nparray3D, filter out the elements that are divisible 
# by 3, and save it as nparray6a. What is the shape of nparray6a?
# remember to print the result
#
# write your codes here
#

#%%
# 6.8) Instead of getting a flat array structure, can you try to perform the filtering 
# in 6.7, but resulting in a numpy array the same shape as nparray3D? Say if a number 
# is divisible by 3, keep it. If not, replace by zero. Try.
# Save the result as nparray6b
# remember to print the result
# 
# write your codes here
#
# 
# ######  END of QUESTION 6    ###   END of QUESTION 6   ##########

#%%
#
