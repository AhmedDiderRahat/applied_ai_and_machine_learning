
# coding: utf-8

# In[19]:


#Basically file handing has three major operation. 1) open, 2) read/write, and 3) close

#File Open
f = open('test.txt', 'w')

f.write('My name is Rahat\n')
f.write('And I a not a data scientist')

f.close()

#File read
f = open('test.txt', 'r')
data = f.read()
f.seek(0)
f.close()

print(data)


# In[20]:


#Rename a file

import os

os.rename('test.txt', 'my_text.txt')
f = open('my_text.txt', 'r')
print(f.read())
f.close()


# In[21]:


#Remove a file

os.remove('my_text.txt')


# In[23]:


#Get Current Directory

print(os.getcwd())


# In[30]:


#Change current working directory

os.chdir("/Users/DELL/python_codes")


# In[31]:


print(os.getcwd())

