
# coding: utf-8

# In[1]:

# Impoting the required python packages
import json
import pandas as pd
import ast
import pprint
import numpy as np


# In[2]:

# Reading the data from the json file
data_120 = pd.read_json('/home/ram/ida.jsonl',lines = True)


# In[3]:


data_120


# In[4]:

#Checking for null values
data_120['address'].isnull().values.any()


# In[5]:


data_021 = data_120['address'].dropna()


# In[6]:

# Checking the rows and columns of the data
data_021.shape[0]


# In[7]:


data_120.shape[0] - data_021.shape[0]


# In[8]:


data_1 = pd.read_json(data_120['address'].to_json())
data_2 = data_1.transpose()


# In[9]:


data_2


# In[93]:

# Making a copy of the data
data_144 = data_2.copy()
data_441 = data_2.copy()


# In[11]:


lis = []
count = 0
for i in range(150000) :
    if (str(data_144['city'][i]) ==  str(data_144['state'][i])
    and str(data_144['state'][i]) == str(data_144['street'][i]) and
    str(data_144['street'][i]== str(data_144['zip'][i]))) :
        data_2['city'][i] = np.nan
        count = count + 1
        lis.append(i)


# In[12]:


for i in lis :
    print(data_2.loc[i])


# In[14]:


count


# In[15]:


count - 13574


# The percentage of records with adress fields is 50.128.

# In[16]:


(float) (count-13574)/(data_2.shape[0])*100


# In[17]:


for i in range(150000) :
    if (str(data_144['state'][i]) ==  str(data_144['street'][i]) ) :
        data_2['state'][i] = np.nan


# In[18]:


for i in range(150000) :
    if (str(data_144['street'][i]) ==  str(data_144['state'][i]) ) :
        data_2['street'][i] = np.nan


# In[19]:


for i in range(150000) :
    if (str(data_144['zip'][i]) ==  str(data_144['street'][i]) ) :
        data_2['zip'][i] = np.nan



# In[20]:


data_341 = data_2.copy()
data_341


# In[21]:


data_341.shape


# In[22]:


data_1000 = data_341.dropna()


# The percentage of records with address.state, address.street, address.zip fields is 40.822.

# In[23]:


(float) (data_1000.shape[0])/(data_341.shape[0]) * 100


# In[24]:


data_1000.shape


# In[25]:


data_341


# In[26]:


str(data_341['city'][100008]) == str(np.nan)


# In[27]:


data_3 = pd.read_json(data_120['name'].to_json() )


# In[28]:


data_4 = data_3.transpose()


# In[135]:


data_4
data_644 = data_4.copy()


# In[30]:


count_2 = 0
sil = []
data_41 = data_4.copy()
for i in range(150000) :
    if((str(data_41['firstname'][i]) == str(data_41['lastname'][i]))
     and (str(data_41['lastname'][i]) == str(data_41['middlename'][i]))) :
                           count_2 = count_2 + 1
                           sil.append(i)


# In[134]:


count_2
len(sil)


# In[141]:


(float) (44996)/(150000)


# In[32]:


str(data_41['firstname'][100]) ==  str(data_41['lastname'][100])


# In[33]:


for i in sil :
    print(data_4.loc[i])


# In[142]:


sil_2 = []
for i in sil :
    if (str(data_4['firstname'][i]) == str(np.nan) and
    str(data_4['lastname'][i]) == str(np.nan) and str(data_4['middlename'][i]) == str(np.nan) ) :
        sil_2.append(i)


# In[143]:


len(sil_2)


# In[133]:


count_3 = 0
for i in sil_2 :
        count_3 = count_3 +1
        print(data_4.loc[i])


# The percentage of records with name field is 28.705.

# In[136]:


count_2 - count_3


# In[131]:


float (count_2-count_3)/(data_4.shape[0]) * 100


# The percentage of records with name.firstname field is 70.002

# In[39]:


data_41fn = data_644['firstname'].copy()
data_41fn = data_41fn.dropna()
data_41fn.shape


# In[145]:


(float) ((data_41fn.shape[0])-(43058))/ (data_4.shape[0])*100


# In[41]:


data_41ln = data_4['lastname'].copy()
data_41ln = data_41ln.dropna()
data_41ln.shape


# The percentage of records with name.lastname field is 70.002

# In[146]:


(float) ((data_41ln.shape[0])-43058)/ (data_4.shape[0]) *100


# In[43]:


data_41mn = data_4['middlename'].copy()
data_41mn = data_41mn.dropna()
data_41mn.shape


# The percentage of records with name.middlename field is 29.112

# In[147]:


(float) ((data_41mn.shape[0])-43058) / (data_4.shape[0]) * 100


# The number of records with dob field is 95.916

# In[46]:


data_dob = data_120['dob'].copy()
data_dob = data_dob.dropna()
data_dob.shape


# In[47]:


(float) (data_dob.shape[0])/ (data_120.shape[0]) * 100


# The number of records with email field is 87.253.

# In[48]:


data_email = data_120['email'].copy()
data_email = data_email.dropna()
data_email.shape[0]


# In[49]:


(float) (data_email.shape[0]) / (data_120.shape[0])* 100


# In[50]:


data_id = data_120['id'].copy()
data_id = data_id.dropna()

data_id.shape[0]


# The percentage of records with id field is 100.

# In[51]:


data_phone = data_120['phone'].copy()
data_phone = data_phone.dropna()
data_phone.shape[0]


# In[52]:


(float) (data_phone.shape[0])/data_120.shape[0]* 100


# The percentage of records with phone field is 93.507

# In[53]:


data_record = data_120['record_date'].copy()

data_record = data_record.dropna()

data_record.shape[0]


# The percentage of records with record_date field is 100.

# In[54]:


data_ssn = data_120['ssn'].copy()
data_ssn = data_ssn.dropna()
data_ssn.shape


# In[55]:


(float) (data_ssn.shape[0])/(data_120.shape[0])*100


# The percentage of records with ssn field is 94.962

# In[56]:


column_list = []
column_list = (data_120.columns).tolist()


# In[57]:


column_list1 = []
for i in range(len(column_list)) :
     column_list1.append(str(column_list[i]))


# In[58]:


column_list1


# In[59]:


column_list2 = []
column_list2 = (data_2.columns).tolist()


# In[60]:


column_list2


# In[61]:


column_list3 = []
for i in range(len(column_list2)) :
     column_list3.append('address.'+str(column_list2[i]))


# In[62]:


column_list3


# In[63]:


for i in range(len(column_list3)) :
    column_list1.append(column_list3[i])


# In[64]:


column_list1


# In[65]:


column_list4 = []
column_list4 = data_4.columns.tolist()


# In[66]:


column_list4


# In[67]:


for i in range(len(column_list4)) :
    column_list1.append('name.'+str(column_list4[i]))


# In[68]:


column_list1


# In[69]:


data_121 = data_120['address'].dropna()


# In[70]:


data_121.shape


# In[71]:


data_121.shape


# In[72]:


data_2['city'].isnull().values.any()
data_2['state'].shape


# In[73]:


data_131 = data_2['state'].dropna()


# In[74]:


data_341.shape


# In[75]:


data_341.shape[0]


# In[76]:


data_341['city'].isnull().values.any()


# In[77]:


data_431 = data_341.copy()


# In[78]:


data_431 = data_431.dropna()


# In[79]:


data_431.shape


# In[80]:


data_431.shape


# The percentage of records which contain address.city field is 40.822

# In[81]:


(float) (data_431.shape[0])/(data_341.shape[0])


# In[82]:


data_341['state'].shape


# In[83]:


data_341['state'].isnull().values.any()


# In[84]:


data_4311 = data_341['state'].dropna()


# In[85]:


data_4311.shape


# In[86]:


data_unifirstname = data_41fn.copy()


# In[91]:


data_41fn.shape


# In[129]:


data_unifirstname = data_unifirstname.unique()
data_unifirstname.shape


# In[104]:


data_unifirstname.shape


# The number of records with distnict first name is 112067.

# In[92]:


(float) (data_41fn.shape[0]) - (data_unifirstname.shape[0])


# In[94]:


data_street = data_441['street'].copy()


# In[121]:


data_441['street'].shape


# In[96]:


for i in lis :
      data_street = data_street.drop([i])


# In[97]:


data_street.shape


# In[99]:


data_street.isnull().any()


# The number of unique street names is 61233.

# In[124]:


len(data_street[0].unique())
