
# coding: utf-8

# # read_html demo
# We import read_html and use it to read the tables from an FDIC web site into.  It returns a list of DataFrames (one per html table), 
# so we get the first one out, then index by name into the 'City' column, which returns a panda Series object.  We get the length of the Series and the length of cities.unique(), which returns the unique cities.

# In[1]:

from pandas.io.html import read_html


# In[2]:

dfs = read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')


# In[3]:

type(dfs)


# In[4]:

df1 = dfs[0]


# In[5]:

type(df1)


# In[6]:

cities = df1['City']


# In[10]:

type(cities)


# In[7]:

len(cities)


# In[8]:

len(cities.unique())


# In[11]:

type(cities.unique())


# In[1]:

print(df1)


