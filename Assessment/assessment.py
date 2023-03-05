#%%

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

#%%
#importing data as a dataframe
iris_df = pd.read_csv('Iris_Data (2).csv')
iris_df
# %%
#simple EDA

# printing shape of the data frame and finding the data types
print(iris_df.shape)
print(iris_df.dtypes)

#checking for null values
null_counts = iris_df.isnull().sum()
print(null_counts)

#Printing the column heads and first 5 rows
print(iris_df.head())

#column names

print(iris_df.columns)
# %%
# Finding how many irises belong to each species


species_count = iris_df.groupby('Labels').size()

print(species_count)


# %%
# Making a scatterplot of petal length vs sepal length

# Creating a scatter plot with different colors for each label


fig, ax = plt.subplots()

colors = {0:'tab:blue', 1:'tab:purple', 2:'tab:green'}

ax.scatter(iris_df[' Petal Length'], iris_df['Sepal Length'], c=iris_df['Labels'].map(colors))


# # Set the axis labels and title
ax.set_xlabel(' Petal Length')
ax.set_ylabel('Sepal Length')
ax.set_title('Scatter Plot of Petal Length vs. Sepal Length')

# # Display the plot
plt.show()
# %%
#Fitting a regression model predicting 
#sepal lenght based on petal lenght
#petal width and sepal width 

import sklearn
from sklearn import metrics



from sklearn.linear_model import LinearRegression

from sklearn.metrics import r2_score


#Extra Credit

import statsmodels.api as sm
from statsmodels.formula.api import ols

# Fitting the regression model
model = ols('Q("Sepal Length") ~ Q(" Petal Length") + Q("Petal Width") + Q("Sepal Width") + C(Labels)', data=iris_df).fit()

# Printting the model summary
print(model.summary())

#The model was designed to estimate the size of an iris's sepals by the width of their petals, sepals, the lenght of the petals and the iris labels. The R-Square score is high at 0.868, this indicates that the model can account for 86.8% of the variation in speal sizes. The adjusted R-square is a bit lower at 0.863, which implies that the model might be fitting too closely, 

# The F-test score is at 188.8 and its p-value is (2.22e-61). This indicates that the regression model is statistically significaion. Now looking at the coefficients for the predictor variables, the coefficient for the petal lenght (0.8288) implies that a unit increase by one means there will be a 0.82888 unit increase in sepal lenght (assuming all other variables are constant). 
#In sum, the regression model is suitablily fitted for predicting the sepal size based on these predictor variables. 

# %%
#Implementing an Edit-Distance Algorithm 

def hammingDistance(string1, string2):
    if len(string1) != len(string2):
        return "Error: imput must be equal lengths"
    distance = 0
    for i in range(min(len(string1), len(string2))):
        if string1[i] != string2[i]:
            # checking for capitalization switch
            if i != 0 and string1[i].upper() == string2[i].upper():
                distance += 0.5
            else:
                distance += 1
        # checking for S/Z 
        elif string1[i].upper() == 'S' and string2[i].upper() == 'Z':
            continue
        elif string1[i].upper() == 'Z' and string2[i].upper() == 'S':
            continue
    # adding remaining characters in longer string to distance
    distance += abs(len(string1) - len(string2))
    return distance



print(hammingDistance("data Science", "Data Sciency"))
print(hammingDistance("organizing","orGanising"))
print(hammingDistance("AGPRklafsdyweIllIIgEnXuTggzF", "AgpRkliFZdiweIllIIgENXUTygSF"))

# A scenario would be applicable for when anyone is inputting data. They could be typing quickly and mispell or press the wrong key. It determines the number of bits that are different in binary sequences. 

#%%

# count how many of the rows have the words "view" or "perspective" but do not include "bottom", "top", "front" or "rear" in  the text field

import re

# Read the csv file into a pandas dataframe
df = pd.read_csv('patent_drawing data (3).csv')
print(df.columns)



def clean_text(text):
    # Removing any punctuation and convert to lower case
    text = re.sub(r'[^\w\s]','',text).lower()
    # Checking if the text contains the words "view" or "perspective" but not "bottom", "top", "front" or "rear"
    if ('view' in text or 'perspective' in text) and not ('bottom' in text or 'top' in text or 'front' in text or 'rear' in text):
        return True
    else:
        return False

# Creating a new column 'clean_text' with cleaned version of 'text' field
df['clean_text'] = df['text'].apply(clean_text)

# How many of the field descriptions reference a perspective that is not standard (i.e. viewed from the top, bottom, front or rear)? Specifically, write code to count how many of the rows have the words "view" or "perspective" but do not include "bottom", "top", "front" or "rear" in  the text field?
non_standard_perspectives = df['clean_text'].sum()
print("Number of rows with non-standard perspectives:", non_standard_perspectives)

# Grouping the dataframe by 'patent_id' and count the number of unique 'index' values for each group
patent_counts = df.groupby('patent_id')['uuid'].nunique()


# What is the average number of drawing descriptions per patent? 
avg_drawings_per_patent = np.mean(patent_counts)
print("Average number of drawing descriptions per patent:", avg_drawings_per_patent)




# %%


