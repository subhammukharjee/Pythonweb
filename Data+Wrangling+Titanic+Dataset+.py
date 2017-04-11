
# coding: utf-8

# In[3]:

#Title
#This is source


# # Title

# -
# -
# -

# -
# -

# -
# -

# In[7]:

import IPython


# In[8]:

print(IPython.sys_info())


# In[9]:

import pandas as pd


# In[10]:

titanic = pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/datasets/Titanic.csv')


# In[11]:

titanic.head()


# In[12]:

titanic.info()


# In[13]:

del titanic['Unnamed: 0']


# In[14]:

titanic.head()


# In[16]:

titanic[['PClass','Age','SexCode']].head()


# In[18]:

titanic.Age.head()


# In[19]:

tpy=titanic.values


# In[20]:

tpy


# In[21]:

import os as os


# In[22]:

os.getcwd()


# In[25]:

os.chdir('F:\STUDY\Digital_Vidya\Data Analytics\Python-3')


# In[24]:

os.getcwd()


# In[26]:

os.getcwd()


# In[27]:

os.listdir()


# In[28]:

titanic.to_csv('F:\\STUDY\\Digital_Vidya\\Data Analytics\\Python-3\\titanic2.csv', index=False)


# In[29]:

os.listdir()


# In[31]:

titanic.query("PClass=='1st'" and "Survived == 1 ")


# In[36]:

titanic.query("PClass=='1st'" and "Survived == 1 ").count()


# In[35]:

titanic.query("PClass=='3rd' and Survived == 1").count()


# In[37]:

138/711


# In[40]:

pd.crosstab(titanic.PClass,titanic.Survived)


# In[42]:

pd.crosstab(titanic.PClass,titanic.Survived,normalize = 'index')


# In[50]:

titanic.query("PClass=='1st'" and "Sex == 'male' " and "Survived == 1").count()


# In[51]:

titanic.query("PClass=='3rd'" and "Sex == 'male' " and "Survived == 1").count()


# In[52]:

pd.crosstab([titanic.PClass, titanic.Sex], titanic.Survived, margins=True)


# In[58]:

titanic.loc[titanic.Survived==1,'Survived2=']='Alive'


# In[59]:

titanic.head()


# In[60]:

titanic.loc[titanic.Survived!=1,'Survived2']='Dead'


# In[61]:

titanic.head()


# In[ ]:



