
# coding: utf-8

# In[2]:


#initialize set

s = {1, 2, 3, 1, 3}
print(s)


# In[11]:


#initialize set with empty set

s = set()
print(type(s))


# In[12]:


#adding single data to set

s.add(7)
s.add(5)
s.add(2)
print(s)


# In[13]:


#adding multiple data to set

s.update([2,  -1,  8])
print(s)


# In[15]:


#deleting element from set

s.discard(2)
print(s)


# In[16]:


s.remove(2)
print(s)


# In[17]:


# remove and discard both delete an element from set but the major difference is, if the element dosen't exist remove function through error.


# In[18]:


#clear function: remove all the elements from set
s.clear()
print(s)


# In[19]:


#Set Operation

a = {1, 3, 5}
b = {2, 3, 4, 6}


# In[20]:


#Set Union

print(a.union(b))
print(a|b)


# In[21]:


#Set Intersection

print(a.intersection(b))
print(a & b)


# In[22]:


#Set Difference

print(a.difference(b))
print(a-b)


# In[26]:


#Set Symmetric Difference

print(a.symmetric_difference(b))
print(a ^ b)

"""symmetric difference between two set is the set difference of their union and intersection"""


# In[27]:


#Set subset: 

c = {2, 6}

print(c.issubset(a))
print(c.issubset(b))

