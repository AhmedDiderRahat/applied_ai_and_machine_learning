
# coding: utf-8

# In[9]:


#Exception handling is one of the common feature of any programming language. In python we can handle any exception with try ... and except block

import sys

my_list = [2, 'b', 0, 7]

for item in my_list:
    try:
        print('Item is: {} and result is: '.format(item), end='')
        print(2/item)
    except:
        print('Found an error and error is: ', sys.exc_info()[0])


# In[10]:


#Raise an error: it's working same as through in java.

try:
    num = int(input("Enter a positive number: "))
    
    if num <= 0:
        raise ValueError('Error: You enter a negative number')
except ValueError as e:
    print(e)

