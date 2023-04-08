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
print(f"the data types of each column are: {dfhappy.dtypes}")
#we can see that Hrs, Num_children, Family_income_tot are all objects, which should have been numeric.
#Check the results using print(df['col_name'].unique()) to find why. Are any of the responses string value?

print(dfhappy['Num_children'].unique())
print(dfhappy['Family_income_tot'].unique())

# Not all are numerica values, some people wrote out the number causing a string value; for income some refused to say their income also causing a string value. 
#%%
####### Question 3 #########
#If the string value for Hrs suggests nonresponse or missing data, let's replace it with np.NaN. In fact, let's just do it for the whole dataset.

dfhappy['Hrs_convert'] = pd.to_numeric(dfhappy['Hrs'], errors='coerce')
print( dfhappy.Hrs_convert.value_counts(dropna=False) )
print("\nReady to continue.")


#%%
####### Question 4 #########
#Now let's check column 'Num_children'; any string value responses that should be treated as nonresponse? Then converted to NaN.
#if the response is a valid string value, convert it to numeric; if it suggests a range of numeric value, replace it with chi squared distribution
#Hint: se the preprocess.py file under “23SP_DATS6103/mod3/Class09_Preprocess/” as a reference.
def clean_children(x):
  if x.isdigit():
      return int(x)
  if 'Eight' in x:
      return 8 + 2*np.random.chisquare(2)
  return np.nan # catch all, just in case
# end function cleanGssAge
print("\nReady to continue.")

dfhappy['Num_children'] = dfhappy['Num_children'].apply(clean_children)
# df[['age']] = df.apply(cleanDfAge,axis=1) # this works too
print(dfhappy.dtypes)



#%%
####### Question 5 #########
#Repeat the same data cleaning and wrangling process for column 'Family_income_tot', following the steps in the preprocess.py file.
def cleanDfIncome(thisamt): 
    
  thisamt = thisamt.strip()
  if (thisamt == "Lt $1000"): return np.random.uniform(0,999)
  if (thisamt == "$1000 to 2999"): return np.random.uniform(1000,2999)
  if (thisamt == "$3000 to 3999"): return np.random.uniform(3000,3999)
  if (thisamt == "$4000 to 4999"): return np.random.uniform(4000,4999)
  if (thisamt == "$5000 to 5999"): return np.random.uniform(5000,5999)
  if (thisamt == "$6000 to 6999"): return np.random.uniform(6000,6999)
  if (thisamt == "$7000 to 7999"): return np.random.uniform(7000,7999)
  if (thisamt == "$8000 to 9999"): return np.random.uniform(8000,9999)
  if (thisamt == "$10000 - 14999"): return np.random.uniform(10000,14999)
  if (thisamt == "$15000 - 19999"): return np.random.uniform(15000,19999)
  if (thisamt == "$20000 - 24999"): return np.random.uniform(20000,24999)
  if (thisamt == "$25000 or more"): return ( 25000 + 10000*np.random.chisquare(2) )
  return np.nan
# end function cleanGssAge
print("\nReady to continue.")

dfhappy['Family_income_tot'] = dfhappy['Family_income_tot'].apply(cleanDfIncome)
# df[['age']] = df.apply(cleanDfAge,axis=1) # this works too
print(dfhappy.dtypes)
print(dfhappy['Family_income_tot'].unique())

#%%
####### Question 6 #########
#Now check the data distribution for 'Happiness'
#Recode 'Very happy' to 2,'Pretty happy' to 1, and 'Not too happy' to 0, and the rest to null values

print(dfhappy['Happiness'].unique())

def clean_happiness(thisamt): 
 
  if (thisamt == "Pretty happy"): return 1
  if (thisamt == "Very happy"): return 2
  if (thisamt == "Not too happy"): return 0
  return np.nan
# end function cleanDfIncome
print("\nReady to continue.")


dfhappy['inHappiness'] = dfhappy['Happiness'].apply(clean_happiness)

print(dfhappy.dtypes)

print(dfhappy['inHappiness'].unique())


#%%
####### Question 7 #########
# For ballot, we can see that entries are 'ballot a','ballot b', etc. let's trim it down to a,b,c

print(dfhappy['Ballot'].unique())

def clean_Ballot(thisamt): # colname can be 'rincome', 'income' etc
  
 
  if (thisamt == "Ballot a"): return 'a'
  if (thisamt == "Ballot b"): return 'b'
  if (thisamt == "Ballot c"): return 'c'
  if (thisamt == "Ballot d"): return 'd'  
  return np.nan
# end function cleanDfIncome
print("\nReady to continue.")

dfhappy['inBallot'] = dfhappy['Ballot'].apply(clean_Ballot)

print(dfhappy.dtypes)

print(dfhappy['inBallot'].unique())

#%%
####### Question 8 #########
# Now let's make plots. First, we need to remove null values in order to plot, which can be done using dropna() method
dfhappy.dropna()


import seaborn as sns

print(dfhappy.isnull())

print(dfhappy.head())


# Make a boxplot to compare hours worked per week by Marital Status (Hrs)(Marital)

print(dfhappy['Marital'].unique())

sns.boxplot(x='Marital', y='Hrs_convert', data=dfhappy)

#%% Make a violin plot for income category vs happiness (where we treat happiness as a construct on a continuum.
# Look at Lecture 8 notes for examples of violin plots


sns.violinplot(x=dfhappy["Marital"], y=dfhappy["Hrs_convert"])




#%%
####### Question 9 #########
# Conduct significance testing to determine if hours worked per week differ significantly by marital status;
# if so, which group is different signficantly from which?
import numpy as np
import scipy.stats as stats

df9 = dfhappy.dropna(subset=['Hrs_convert', 'Marital'])

#print(df9.describe())
print(df9.isnull().sum())

#print(df9.head())

sns.boxplot(x='Marital', y='Hrs_convert', data=df9)
plt.show()

group1 = df9[df9['Marital'] == 'Never married']['Hrs_convert']
group2 = df9[df9['Marital'] == 'Married']['Hrs_convert']
group3 = df9[df9['Marital'] == 'Divorced']['Hrs_convert']
group4 = df9[df9['Marital'] == 'Never married']['Hrs_convert']
group5 = df9[df9['Marital'] == 'Widowed']['Hrs_convert']
group6 = df9[df9['Marital'] == 'No answer']['Hrs_convert']

print(group1.head())

# ANOVA
f_stat, p_val = stats.f_oneway(group1, group2, group3, group4, group5, group6)

print("F statistic:", f_stat)
print("p-value:", p_val)


# As we see, the p-value is less than 0.05, meaning there is a sgnificant difference in the hours worked a week by marital status. 

#To find out which group is significant I will do a Tukey HSD Test
import statsmodels.stats.multicomp as mc

from statsmodels.formula.api import ols


groups = [group1, group2, group3, group4, group5, group6]
group_labels = ['Never married', 'Married', 'Divorced', 'Widowed', 'No answer']

data = pd.concat(groups, keys=group_labels)

data = data.reset_index(level=[0])

model = ols('Hrs_convert ~ C(level_0)', data=data).fit()

mc_object = mc.MultiComparison(data['Hrs_convert'], data['level_0'])

tukey_result = mc_object.tukeyhsd()

tukey_df = pd.read_html(tukey_result.summary().as_html(), header=0, index_col=0)[0]

significant_differences = tukey_df[tukey_df["reject"]]

print(significant_differences)

#%%
####### Question 10 #########
### Do whatever you can to find out if number of children is dependent on happiness and/or if happiness is dependent on number of children..

df10 = dfhappy.dropna(subset=['Num_children', 'inHappiness'])

print(df10.head())


group1 = df10[df10['inHappiness'] == 0]['Num_children']
group2 = df10[df10['inHappiness'] == 1]['Num_children']

t_stat, p_value = stats.ttest_ind(group1, group2)

# Print the results
print("t-statistic:", t_stat)
print("p-value:", p_value)

#P-value is less than 0.05, so there is a significant difference between the number of children and happiness. 


# %%
