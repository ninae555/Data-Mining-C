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
#`survived`: Survival,	0 = No, 1 = Yes
# * `pclass`: Ticket class, 1 = 1st, 2 = 2nd, 3 = 3rd
# * `sex`: Gender / Sex
# * `age`: Age in years
# * `sibsp`: # of siblings / spouses on the Titanic
# * `parch`: # of parents / children on the Titanic
# * `ticket`: Ticket number (for superstitious ones)
# * `fare`: Passenger fare
# * `embarked`: Port of Embarkment	C: Cherbourg, Q: 
view = titanic.head
print(view)



import statsmodels.formula.api as smf

model = smf.logit('survived ~ sex + age + pclass + sibsp + parch', data=titanic).fit()

print(model.summary())

# I can see that parch is not significant with a P-value at 0.835. So I will remove it from my model. 
model = smf.logit('survived ~ sex + age + pclass + sibsp', data=titanic).fit()

print(model.summary())


#%% 
# Question 3
# Interpret your result. 
# What are the factors and how do they affect the chance of survival (or the survival odds ratio)? 
# What is the predicted probability of survival for a 30-year-old female with a second class ticket, 
# no siblings, 3 parents/children on the trip? Use whatever variables that are relevant in your model.
# 
# 
print(model.summary())

# ANALYSIS

modelpredicitons = pd.DataFrame( columns=['survived'], data= model.predict(titanic)) 

modelpredicitons['survivalLogit'] = model.predict(titanic)
print(modelpredicitons.head())

print("\nReady to continue.")

#Female 30 yrs of age, with a second class ticket, no siblings and 3 parents 
age = 30
sex = 'female'
pclass = 2
sibsp = 0
parch = 3

# Scenario values
scenario_df = pd.DataFrame({'age': [age], 'sex': [sex], 'class': [pclass], 'sibsp': [sibsp], 'parch': [parch]})


predicted_probabilities = model.predict(scenario_df)

predicted_probability = predicted_probabilities[0]

print("Predicted probability of survival:", predicted_probability)



#%%
# Question 4
# Now use the sklearn package, perform the same model and analysis as in Question 3. 
# In sklearn however, it is easy to set up the train-test split before we build the model. 
# Use 67-33 split to solve this problem. 
# Find out the accuracy score of the model.
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OneHotEncoder

# column_name = 'sex'  # 
# search_string = 'STON/O 2. 3101293'
# result = titanic[titanic[column_name].str.contains(search_string, na=False)]

# Display the resulting DataFrame
# print(result)


#Converting categorical string into categorical numeric value 


titanic_onehot = pd.get_dummies(titanic, columns = ['sex'])
print(titanic_onehot)

# type = titanic_onehot['sex'].dtypes
# print(type)
# type = titanic_onehot['survived'].dtypes
# print(type)

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(titanic_onehot.drop('survived', axis=1), titanic_onehot['survived'], test_size=0.2, random_state=42)

# Creating an instance of LogisticRegression
model = LogisticRegression()

# Training the model on the training set
model.fit(X_train, y_train)

# Making predictions on the testing set
y_pred = model.predict(X_test)

# Evaluating the model's accuracy
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)

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

