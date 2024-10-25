#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Importing libraries/modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[6]:


df = pd.read_csv("TickTok Dataset 2.csv", encoding="ISO-8859-1")
df.head()


# In[7]:


#correcting the column to a proper column writting format.
column_mapping = {'Video Duration':'Video_Duration','Average Views':'Average_Views','Net Worth(Million)':'Net_Worth(Million)','Most Viewed Video(Billion)':'Most_Viewed_Video(Billion)','Most Liked Video(Million)':'Most_Liked_Video(Million)','Video Category':'Video_Category'}

# Rename the columns using the rename method
data = df.rename(columns=column_mapping)

# Verify the changes
print(data.columns)


# In[8]:


data.head(10)


# # checking out the data

# In[10]:


data.info()


# In[16]:


#checking the shape of our data
data.shape


# In[18]:


#checkiing if the data has missing values
data.isnull().sum()


# In[20]:


#have the descriptive statistics about our data
data.describe()


# # Exploratory Data Analysis

# 1. we first want to check which celebrity has a lot of followers.

# In[62]:


# Insighting for Individual Columns

# Followers
followers_min = data['Followers'].min()
followers_max = data['Followers'].max()
followers_mean = data['Followers'].mean()
print(followers_min)
print(followers_max)
print(followers_mean)


# In[64]:


# Following

following_min = data['Following'].min()
following_max = data['Following'].max()
print(f"\nFollowing:\nRange: {following_min} to {following_max}")


# In[66]:


# Likes
likes_min = data['Likes'].min()
likes_max = data['Likes'].max()
likes_mean = data['Likes'].mean()
print(f"\nLikes (in billions):\nRange: {likes_min}B to {likes_max}B, Mean: {likes_mean}B")


# In[24]:


top_follower_celebrity = data[data["Followers"] == data["Followers"].max()]
top_follower_celebrity


# From the results above, we can see that Khaby.lame has most followers among the celebrities

# In[27]:


# Sort the DataFrame by the 'Followers' column in descending order and select the top 10 rows
top_10_followed_celebrities = data.sort_values(by='Followers', ascending=False).head(10)

# Display the result
top_10_followed_celebrities


# In[29]:


#changing the data type of the Net_worth column so that we can perfome the correlation on it
data['Net_Worth(Million)'] = pd.to_numeric(data['Net_Worth(Million)'], errors='coerce')
# Check the data type to confirm
print(data['Net_Worth(Million)'].dtype)


# In[31]:


data.info()


# In[33]:


#checkiing if the data has missing values
data.isnull().sum()


# In[35]:


data.dropna(inplace=True, axis=0)
#checkiing if the data has missing values
data.isnull().sum()


# Now we can inspect if there is a correlation between in the number of views and the net_worth

# In[38]:


# Calculate the correlation between 'Average_Views' and 'Net_Worth(Million)'
correlation = data['Followers'].corr(data['Net_Worth(Million)'])
print("Correlation between Followers and Net Worth:", correlation)


# Since the correlation is very small, we can say that number of followers each celebrity has, does not depend on how worth they are.

# In[41]:


# Prepare the data
x = data['Followers']
y = data['Net_Worth(Million)']

# Calculate the line of best fit
slope, intercept = np.polyfit(x, y, 1)
line = slope * x + intercept

# Create the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', s=50, label='Data Points')  # Scatter plot
plt.plot(x, line, color='red', label='Line of Best Fit')  # Line of best fit

# Set labels and title
plt.xlabel('Followers')
plt.ylabel('Net Worth (Million)')
plt.title('Correlation between Followers and Net Worth')
plt.legend()

# Show plot
plt.show()


# In[46]:


# 3. Histogram of Followers
plt.hist(df["Followers"], bins=5, color='skyblue')
plt.xlabel("Followers (Millions)")
plt.ylabel("Frequency")
plt.title("Distribution of Followers")
plt.show()



# In[54]:


# Net Worth vs. Followers
plt.scatter(data["Net_Worth(Million)"], data["Followers"], color='coral')
plt.xlabel("Net Worth (Million)")
plt.ylabel("Followers (Millions)")
plt.title("Net Worth vs. Followers")
plt.show()


# In[58]:


#Duration vs. Average Views
plt.scatter(data["Average_Views"], data["Likes"], color='purple')
plt.xlabel("Average Views (Millions)")
plt.ylabel("Likes (Millions)")
plt.title("Average Views vs. Likes")
plt.show()


# In[ ]:




