# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'

#%% [markdown]
#
# # HW Pandas - grades
# ## By: Nina Ebensperger
# ### Date: March 1st, 2023
#

#%% [markdown]
# Let us improve our Stock exercise and grade conversion exercise with Pandas now.
#

#%%


import rfit
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#%%
# Re-solve the grade-changing exercise (calculating GPA)
# First, load the data frame

dats = rfit.dfapi('Dats_grades')
rfit.dfchk(dats)


#%%
# What are the variables in the df? 
# What are the data types for these variables?
#
# The file has grades for a DATS class. Eight homeworks (out of 10 each), 2 quizzes (out of 100 each), and 2 projects (out of 100 each)
# Find out the class average for each item (HW, quiz, project)
# Hint, use .mean() function of pandas dataframe

# ######  QUESTION 1      QUESTION 1      QUESTION 1   ##########
#Getting columns in dataframe to find the variables
print(f" The following is the list of variables along with the data type: {dats.columns}")

#finding the class average 
#finding mean for HW 
hw_mean_indy = dats[["H1", "H2", "H3", "H4","H5", "H6", "H7", "H8"]].mean()
hw_mean = hw_mean_indy.mean()
print(f"the mean for all homeworks is: {hw_mean}")

#finding mean for quizes 
q_mean_indy = dats[["Q1", "Q2"]].mean()
quiz_mean = q_mean_indy.mean()
print(f"the mean for all quizes is: {quiz_mean}")

#finding mean for project




# ######  END of QUESTION 1    ###   END of QUESTION 1   ##########

#%%
# create a new column right after the last hw column, to obtain the average HW grade
# for each student.
# Name column as HWavg. Make the average out of the total of 100.
# Hint: use .iloc to select the HW columns, and then use .mean(axis=1) to find the row average

# ######  QUESTION 2      QUESTION 2      QUESTION 2   ##########

# write your codes here

# ######  END of QUESTION 2    ###   END of QUESTION 2   ##########

dats.head() # check result


#%%
# The course total = 30% HW, 10% Q1, 15% Q2, 20% Proj1, 25% Proj2. 
# Calculate the total and add to the df as the last column, named 'total', out of 100 max.

# ######  QUESTION 3      QUESTION 3      QUESTION 3   ##########

# write your codes here

# ######  END of QUESTION 3    ###   END of QUESTION 3   ##########

dats.head() # check result

#%%
# Now with the two new columns, calculate the class average for everything again. 

# ######  QUESTION 4      QUESTION 4      QUESTION 4   ##########

# write your codes here

# ######  END of QUESTION 4    ###   END of QUESTION 4   ##########

#%%
# Save out your dataframe as a csv file
# import os

# ######  QUESTION 5      QUESTION 5      QUESTION 5   ##########

# write your codes here

# ######  END of QUESTION 5    ###   END of QUESTION 5   ##########



#%%
# Finally, re-solve our homework exercise for calculating GPA using functions, but with a dataframe now.
# In Week03 hw, we wrote a function to convert course total to letter grades. You can use your own, or the one from the solution file here.
def find_grade(total):
  # write an appropriate and helpful docstring
  """
  convert total score into grades
  :param total: 0-100 
  :return: str
  """
  # ######  QUESTION 6      QUESTION 6      QUESTION 6   ##########

  # copy your codes here, either from your Week03 hw, or the solution file

  # ######  END of QUESTION 6    ###   END of QUESTION 6   ##########
  return # grade  

#%%
# Using the .apply() method in Pandas
# 
# Let us create one more column for the letter grade, just call it grade.
# Instead of broadcasting some calculations on the dataframe directly, we need to apply (instead of broadcast) this find_grade() 
# function on all the elements in the total column
# ######  QUESTION 7      QUESTION 7      QUESTION 7   ##########

# write your code using the .apply() function to obtaine a new column of letter grade (call that new column 'grade') from the total.

# ######  END of QUESTION 7    ###   END of QUESTION 7   ##########



#%%

