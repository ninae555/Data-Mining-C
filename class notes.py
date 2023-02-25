# %%
import pandas as pd
url = "https://raw.githubusercontent.com/ning-rui/23SP_DATS6103/main/mod3/Class06_Pandas/data.csv?token=GHSAT0AAAAAAB432WTULT2E6RJNPRVIADECY7VL57A"
data1 = pd.read_csv(url)
url2 = "https://raw.githubusercontent.com/ning-rui/23SP_DATS6103/main/mod3/Class06_Pandas/data2.csv?token=GHSAT0AAAAAAB432WTUWXGYD73OK6XEKJPWY7VL7SA"
data2 = pd.read_csv(url2)

#Exercise: Calculate the correlation between ‘Duration’ and ‘Maxpulse’, and draw a scatter plot to show the relationship

#%%
# corr=data1['Duration'].corr(data1['Maxpulse'])
# print(corr)
# data1.plot(kind='scatter',x='Duration',y='Maxpulse')

download_url1 = (
"https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv"
)
print(download_url1)
iris = pd.read_csv(download_url1)
iris.info()


# %%



import matplotlib.pyplot as plt

plt.hist(iris['petal.length'],alpha=.5, label='petal length')
plt.hist(iris['sepal.length'],alpha=0.5, label='sepal length') 
plt.legend(loc='upper right')
plt.title('Distribution of petal and sepal length of iris ')
plt.show()


#Create overlapping histograms of sepal width and petal width
plt.hist(iris['petal.width'],alpha=.5, label='petal length')
plt.hist(iris['sepal.width'],alpha=0.5, label='sepal length') 
plt.legend(loc='upper right')
plt.title('Distribution of petal and sepal width of iris ')
plt.show()

# %%
# Create a data frame using the publicly available dataset ‘recent_grad.csv’

# *Download the data file and create the df
download_url = ( "https://raw.githubusercontent.com/fivethirtyeight/data/master/college-majors/recent-grads.csv"
)

df = pd.read_csv(download_url)


# %%
# Q1: displayed the first 15 rows of the DataFrame 

df.head(15)

# Q2: Show distribution of total enrollment and correlation of male and female enrollment; create a scatter plot of male and female enrollment

df.plot()

corr = df['Women'].corr(df['Men'])
print(corr)

df.plot(kind = 'scatter', x = 'Men', y = 'Women')

# Class answer

df['Men'].corr(df['Women'])

df.plot(kind='scatter',x='Men',y='Women')

plt.scatter(x=df['Total'],y=df['Men'], c='blue')
plt.scatter(x=df["Total"],y=df["Women"], c='red')
plt.xlabel('Total Enrollment')
plt.ylabel('Gender')
plt.title("Distribution of Men and Female of Total enrollment")
plt.show()x





#%%

# Q3: Create a histograms of male and female enrollment with different labels to see how much overlap there is between them

plt.hist(df['Women'],alpha=.5, label = 'female')
plt.hist(df['Men'],alpha=.5, label = 'male')
plt.legend(loc='upper right')
plt.title('Histogram of Make and Female enrollement')
plt.show()

# %%
