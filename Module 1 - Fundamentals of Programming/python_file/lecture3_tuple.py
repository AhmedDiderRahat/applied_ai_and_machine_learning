
# coding: utf-8

# In[11]:


#initializing tuple

t = 1,
print(t)

type(t)


# In[18]:


#tuple data access

data = (5, ("Rahat", "Ahmed", "Dider", (7, 8, 1993)))
print(data[1][3][1])


# In[21]:


#tuple is immutable. So if we need to update tuple, we have to change the type of tuple
tData = list(data)
tData[0] = -3.15
data = tuple(tData)
print(data)


# In[27]:


#concatening tuple

data1 = (1, 2, 3)
data2 = (3, 4, 5, 6)

data3 = data1 + data2

data3


# In[28]:


#deleting a tupe

del data3


# In[39]:


#count

data = (1, 3, 8, 7, 1, 5, 3, 6, 1)

print(data.count(1))


# In[40]:


#tuple index: return the first occurance of any element from a tuple
print(data.index(3))


# In[41]:


#in/not in: return an element exist or not in atuple

print(7 in data)
print(7 not in data)


# In[42]:


#tuple lenght: return the length of the tuple
print(data)
print(len(data))


# In[48]:


#tuple sort: sort the tuple in accending order. sorted function always return a list. So, have to convert it to tuple again
data = tuple(sorted(data))
print(data)


# In[49]:


#maximum of a tuple
print(max(data))


# In[50]:


#minimum of a tuple
print(min(data))


# In[51]:


#summation of a tuple
print(sum(data))

