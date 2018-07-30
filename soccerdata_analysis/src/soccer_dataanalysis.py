
# coding: utf-8

# In[2]:

# Importing the required python packages
import sqlite3
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt
import matplotlib.pyplot as plt


# In[3]:

# Getting the data from a data base

cnx = sqlite3.connect('/home/ram/database.sqlite')
df = pd.read_sql_query("SELECT * FROM Player_Attributes", cnx)


# In[4]:

# Checking the data
df


# In[5]:

# Checking the number of rows and columns of the data
df.shape


# In[6]:

# Checking the fields or columns of the data
df.columns


# In[7]:

# Dropping the null values
df= df.dropna()


# In[8]:


df.shape


# In[9]:

# Finding the correlation between vision and penalties of the soccer players
df['vision'].corr(df['penalties'])


# In[10]:

# Creating a cleanup_rate dictionary
cleanup_rate= {"attacking_work_rate": {"high": 2,"medium": 1,"low": 0},
               "defensive_work_rate": {"high": 2,"medium": 1,"low": 0},
               "preferred_foot": {"right": 1, "left": 0} }


# In[11]:


df.replace(cleanup_rate, inplace=True)
df.head()


# In[12]:


df


# In[13]:

#Calculating the average of the right foot players rating
avg_right= df.loc[df['preferred_foot'] == 1, 'overall_rating'].copy()


# In[14]:
# Calculating the mean

avg_right.mean()


# In[15]:

#Calculating the average of the left foot players rating

avg_left= df.loc[df['preferred_foot'] == 0, 'overall_rating'].copy()


# In[16]:


avg_left.mean()


# Defensive_work_rate= "low" is labeled 0 and "medium" is labeled 1

# In[17]:


avg_penalties_lowdefense= df.loc[df['defensive_work_rate'] == 0, 'penalties'].copy()


# In[18]:

# Calculating the mean of the low defense players penalties
avg_penalties_lowdefense.mean()


# In[19]:


avg_penalties_mediumdefense= df.loc[df['defensive_work_rate'] == 1, 'penalties'].copy()


# In[20]:

# Calculating the mean of the medium defense players penalties
avg_penalties_mediumdefense.mean()
