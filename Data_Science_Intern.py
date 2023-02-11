#%%
import pandas as pd
import numpy as np
# %%
df = pd.read_csv('/Users/admin/Downloads/Data Science Sample Data - Sheet1.csv')

# %%
print(df.head())
print(df.describe())
print(df.info())
# %%
# we can see that there is a missing value for checkinDatTime column
print(df['Check in DateTime'])

# %%
df['Check in DateTime'].fillna('1/6/2023 4:00 PM', inplace=True)
# %%

# 11th value is incorrect in this column

df['Check in DateTime'].iloc[11] = '1/15/2023 4:00 PM'
# %%
print(df['Check in DateTime'])

# %%
print(df['Check in Note'])
# %%
df['Check in Note'].fillna('No Notes made on this day',inplace=True)
# %%

# Storing the clean data
#%%
import altair as alt
import matplotlib as plt
df.plot(y = "Check in %", x = 'Check in DateTime')

a = alt.Chart(df).mark_line().encode(
    x = alt.X('Check in DateTime', type='temporal'),
    y = alt.Y('Check in %', type='quantitative'),
    tooltip = ['Intention (Boolean):O','Check in Note: O']
)
a
#df.to_csv()
# %%
df.info()
# %%
df['Check in Datetime'] = pd.to_datatime()