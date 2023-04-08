# To add a new cell, type ''
# To add a new markdown cell, type '#%%[markdown]'

#%%[markdown]
#
# # HW Regression
# ## By: Nina Ebenspreger
# ### Date: April 8, 2023
#
# 
# We have the historic Titanic dataset to study here. You can use `Titanic` with rfit.dfapi
# to load the dataset, or if given, from local file `Titanic.csv`.  
# The variables in the dataset are:  

# * `survival`: Survival,	0 = No, 1 = Yes
# * `pclass`: Ticket class, 1 = 1st, 2 = 2nd, 3 = 3rd
# * `sex`: Gender / Sex
# * `age`: Age in years
# * `sibsp`: # of siblings / spouses on the Titanic
# * `parch`: # of parents / children on the Titanic
# * `ticket`: Ticket number (for superstitious ones)
# * `fare`: Passenger fare
# * `embarked`: Port of Embarkment	C: Cherbourg, Q: Queenstown, S: Southampton
#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import rfit 


#%%
# Question 1
# Load the Titanic dataset
titanic = rfit.dfapi('Titanic','id')
# then perform some summary statistics. 
# a)	Histogram on age. Maybe a stacked histogram on age with male-female as two series if possible
sns.histplot(data=titanic, stat="count", multiple="stack", x="age", kde=False, palette="pastel", hue="sex",element="bars", legend=True, bins=50)
plt.title("Stacked Histogram of age by gender")
plt.show()


# b)	proportion summary of male-female, survived-dead
sex_counts = titanic['sex'].value_counts()
plt.pie(sex_counts, labels=sex_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Proportional Summary of Sex on Titanic')
plt.show()


# c)	pie chart for “Ticket class”
pclass_counts = titanic['pclass'].value_counts()
plt.pie(pclass_counts, labels=pclass_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Pie chart of Ticket Class on Titanic')
plt.show()

# d)	A single visualization chart that shows info of survival, age, pclass, and sex.

fig, axs = plt.subplots(nrows=2, figsize=(8, 10))


sns.violinplot(data=titanic, x=titanic["pclass"], y=titanic["age"], hue='sex', palette=['cornflowerblue', 'indianred'], ax=axs[0])
axs[0].set(xlabel='', ylabel='Age', title='Age Distribution by Pclass and Adult Male')


sns.violinplot(data=titanic, x=titanic["pclass"], y=titanic["age"], hue='survived', palette=['cornflowerblue', 'indianred'], ax=axs[1])
axs[1].set(xlabel='Class', ylabel='Age', title='Age Distribution by Pclass and Survival Status')


axs[0].set(xlabel='')
axs[1].set(ylabel='')

sns.despine()

plt.subplots_adjust(hspace=0.4)

plt.show()




# %%
# Question 2
# Using the statsmodels package, 
# build a logistic regression model for survival. Include the features that you find plausible. 
# Make sure categorical variables are use properly. If the coefficient(s) turns out insignificant, drop it and re-build.
# 
import statsmodels as sm



#%% 
# Question 3
# Interpret your result. 
# What are the factors and how do they affect the chance of survival (or the survival odds ratio)? 
# What is the predicted probability of survival for a 30-year-old female with a second class ticket, 
# no siblings, 3 parents/children on the trip? Use whatever variables that are relevant in your model.
# 
# 
# 
#%%
# Question 4
# Now use the sklearn package, perform the same model and analysis as in Question 3. 
# In sklearn however, it is easy to set up the train-test split before we build the model. 
# Use 67-33 split to solve this problem. 
# Find out the accuracy score of the model.
# 
# 
# 
#%%
# Question 5
# Try three different cut-off values at 0.3, 0.5, and 0.7. What are the 
# a)	Total accuracy of the model
# b)	The precision of the model for 0 and for 1
# c)	The recall rate of the model for 0 and for 1
# 
# 
#%% 
# Question 6
# By using cross-validation, re-do the logit regression, and evaluate 
# the 10-fold average accuracy of the logit model. 
# Use the same predictors you had from previous questions.
#
#

