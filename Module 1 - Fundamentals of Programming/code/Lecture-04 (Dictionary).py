
# coding: utf-8

# In[1]:


"""Dictionary is an unorder collection of items. Its contains the data using key-value pair"""


# In[2]:


#dictionary with simple key-value
student = {"name" : "Rahat", "id": 24066, "age" : 26.8}
print(student)


# In[3]:


#dictionary with complex data as value

complex_dict = {"name" : "Adi", "results" : [('math', 3.5), ('phy', 4)]}
print(complex_dict)


# In[5]:


#dictionary with no data

empty_dict = dict()
print(empty_dict)


# In[6]:


#dictionary creation with List

dict_list = dict([("Rahat", 3.68), ("Baser", 3.86)])
print(dict_list)


# In[7]:


#dictionary access

print(dict_list["Rahat"])


# In[9]:


"""If key is not found"""

print(dict_list["rahat"])


# In[10]:


#dictionary access with get method

print(dict_list.get("Rahat"))


# In[11]:


print(dict_list.get("rahat")) #the key is not available in dict.


# In[13]:


"""We can access any element by dict[key] or dict.get() function. If the key is not available, then direct access make key exception. On the other hand get function couldn't through exception instead of return a None"""


# In[15]:


#adding element in dictionary

dict_list["hasina"] = 2.74
print(dict_list)


# In[16]:


#updating element in dictionary

dict_list["hasina"] = 2.28
print(dict_list)


# In[17]:


#deleting an item from dictionary using pop function

dict_list.pop("Baser")
print(dict_list)


# In[23]:


dict_list.pop("Baser")

"""If the item is not in the dictionary. it will through exception"""


# In[24]:


del dict_list["Baser"]

"""If the item is not in the dictionary. it will through exception"""


# In[26]:


#deleting all items using clear

dict_list.clear()
print(dict_list)


# In[27]:


#deleting all items using del function

dict_list = dict([("Rahat", 3.68), ("Baser", 3.86)])
print(dict_list)

del dict_list
print(dict_list)


# In[29]:


"""Major difference between del function and clear is: clear remove all the elements and make the dictionary empty otherwise del function remove the dictionary from the memory location"""


# In[31]:


"""Dictionary Methods..."""

square = {2: 4, 3: 9, 4: 16, 5: 25}


# In[32]:


#copy method

new_dict = square.copy()
print(new_dict)


# In[34]:


#fromkeys(sequence, value)

new_dict = {}.fromkeys(['rahat', 'munna', 'munni'], 0)
print(new_dict)


# In[36]:


#items function return all the elemennts and their value as the list of pair(tuple)

print(square.items())


# In[37]:


#keys function return all the keys in a list

print(square.keys())


# In[38]:


#values function return all the values in a list

print(square.values())


# In[39]:


#get all the build in methods of dictionary

d = {}
print(dir(d))


# In[43]:


"""Dictionary Comprehension"""

st_dict = {"a" : 1, "b": 2, "c" : 3, "d": 4}


# In[45]:


#create dict using loop

new_dict = {key:value for key, value in st_dict.items() if value%2 == 0}
print(new_dict)

