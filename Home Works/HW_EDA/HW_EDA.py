# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'

#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import dm6103 as dm

# The dataset is obtained from 
# https://gssdataexplorer.norc.org 
# for you here. But if you are interested, you can try get it yourself. 
# create an account
# create a project
# select these eight variables: 
# ballot, id, year, hrs1 (hours worked last week), marital, 
# childs, income, happy, 
# (use the search function to find them if needed.)
# add the variables to cart 
# extract data 
# name your extract
# add all the 8 variables to the extract
# Choose output option, select only years 2000 - 2018 
# file format Excel Workbook (data + metadata)
# create extract
# It will take some time to process. 
# When it is ready, click on the download button. 
# you will get a .tar file
# if your system cannot unzip it, google it. (Windows can use 7zip utility. Mac should have it (tar function) built-in.)
# Open in excel (or other comparable software), then save it as csv
# So now you have Happy table to work with
#
# When we import using pandas, we need to do pre-processing like what we did in class
# In this assignment, I'd you to first clean up the columns.
# You can use some of the functions we defined in 'Preprocess.py' that we discussed in Lecture9, such as total family income, and number of children. 
# Other ones like worked hour last week, etc, you'll need a new function. 
# Happy: change it to numeric codes (ordinal variable)
# Ballot: just call it a, b, or c 
# Marital status, it's up to you whether you want to rename the values. 
#

# After the preprocessing, make these plots
# Box plot for hours worked last week, for the different marital status. (So x is marital status, and y is hours worked.) 
# Violin plot for income vs happiness, 
# (To use the hue/split option, we need a variable with 2 values/binomial, which 
# we do not have here. So no need to worry about using hue/split for this violinplot.)
# Use happiness as numeric, make scatterplot with jittering in both x and y between happiness and number of children. Choose what variable you want for hue/color.
# If you have somewhat of a belief that happiness is caused/determined/affected by number of children, or the other 
# way around (having babies/children are caused/determined/affected by happiness), then put the dependent 
# variable in y, and briefly explain your choice.
#First, import the dataframe
dfhappy = dm.api_rfit('Happy') 



#%%
####### Question 1 #########
# First, familiarize yourself with the data structure
# Optimize nomenclature by renaming columns to 'Year','ID','Hrs','Marital','Num_children','Family_income_tot','Happiness','Ballot'
# Check your results
dfhappy.describe()
dfhappy.head()

dfhappy = dfhappy.rename(columns= {'year':'Year', 'id':'ID','hrs1':'Hrs','marital':'Marital','childs':'Num_children', 'income':'Family_income_tot','happy':'Happiness','ballet':'Ballot'})

dfhappy.head()

#%%
####### Question 2 #########
#Check datatype of each column, what data types are they?

#we can see that Hrs, Num_children, Family_income_tot are all objects, which should have been numeric.
#Check the results using print(df['col_name'].unique()) to find why. Are any of the responses string value?

#%%
####### Question 3 #########
#If the string value for Hrs suggests nonresponse or missing data, let's replace it with np.NaN. In fact, let's just do it for the whole dataset.
#after you are done, pls check and ensure the column is now numeric
#Hint: use the preprocess.py file under “23SP_DATS6103/mod3/Class09_Preprocess/” as a reference.

#%%
####### Question 4 #########
#Now let's check column 'Num_children'; any string value responses that should be treated as nonresponse? Then converted to NaN.
#if the response is a valid string value, convert it to numeric; if it suggests a range of numeric value, replace it with chi squared distribution
#Hint: se the preprocess.py file under “23SP_DATS6103/mod3/Class09_Preprocess/” as a reference.

#%%
####### Question 5 #########
#Repeat the same data cleaning and wrangling process for column 'Family_income_tot', following the steps in the preprocess.py file.


#%%
####### Question 6 #########
#Now check the data distribution for 'Happiness'
#Recode 'Very happy' to 2,'Pretty happy' to 1, and 'Not too happy' to 0, and the rest to null values

#%%
####### Question 7 #########
# For ballot, we can see that entries are 'ballot a','ballot b', etc. let's trim it down to a,b,c

#%%
####### Question 8 #########
# Now let's make plots. First, we need to remove null values in order to plot, which can be done using dropna() method
# Make a boxplot to compare hours worked per week by Marital Status
# Make a violin plot for income category vs happiness (where we treat happiness as a construct on a continuum.
# Look at Lecture 8 notes for examples of violin plots

#%%
####### Question 9 #########
# Conduct significance testing to determine if hours worked per week differ significantly by marital status;
# if so, which group is different signficantly from which?
#%%
####### Question 10 #########
### Do whatever you can to find out if number of children is dependent on happiness and/or if happiness is dependent on number of children