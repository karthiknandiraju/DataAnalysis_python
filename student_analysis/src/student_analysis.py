
# coding: utf-8

# In[26]:

# Importing the necessary python packages
import sqlite3
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt


# In[27]:

# Reading the data from the csv file on my local machine
data = pd.read_csv('/home/ram/stud.csv')


# In[28]:

# Checking the data
data


# In[29]:

# Deleting the unnecessary columns or fields
del data['Diplogpa']


# In[30]:

# Checking the data
data


# In[31]:

#cheking the colums present in the data
data.columns


# In[32]:

# Performing data wrangling or feature selection
features= [ 'SNO', 'CID', 'firstname', 'lastname', 'fullname', 'Gender', 'EMAILID',
       'MobileNo', 'DOB', 'National', 'Colname', 'University', 'GPAX', 'XYEAR',
       'GPAXII', 'XIIYEAR', 'Current', 'Degree',
       'Specialization', 'UGGPA']


# In[33]:


pd= data[features]


# In[34]:

#Removing Null values
pd= pd.dropna()


# In[41]:

# Selecting the x features(10 grade and 12 grade gpa) for regression
x_features= ['GPAXII','GPAX']


# In[42]:


x= pd[x_features]


# In[45]:

# Selecting the y features(undergraduate gpa) for regression
y_features= ['UGGPA']


# In[46]:


y= pd[y_features]


# In[48]:

#Regression
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=324)


# In[49]:

#checking the training data
X_train.head()


# In[53]:

# Training the regression model using regression data
regressor = LinearRegression()
regressor.fit(X_train[:500], y_train[:500])


# In[54]:

# Getting the predictions
y_prediction = regressor.predict(X_test)
y_prediction


# In[55]:

# Checking the predicted undergraduate gpa Values
y_test.describe()


# In[73]:

# Checking the root mean sqaure error
RMSE = sqrt(mean_squared_error(y_true = y_test[:40], y_pred = y_prediction[:40]))


# In[71]:
# Printing the root mean sqaure error value
print(RMSE)
