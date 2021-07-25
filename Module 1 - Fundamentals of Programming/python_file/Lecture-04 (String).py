
# coding: utf-8

# In[3]:


"""String is a sequence of Unicode characters"""


# In[5]:


#String assignment: we can define string by single, double or triple quotation

string1 = 'Hello world!'
string2 = "Hello world!"
string3 = '''Hello world!'''

print(string1 + " " + string2 + " " + string3)


# In[7]:


#Access element of a string

c1 = string1[0]
c2 = string1[10]
c3 = string1[6:11]

print(c1 + ' ' + c2 + ' ' + c3)


# In[8]:


#Update string or delete elements from string

"""String is immutable. So, we can't update any string"""


# In[9]:


#String delete

del string1


# In[10]:


#String operations

str1 = "Joy"
str2 = "Bangla"


# In[12]:


#Concatenation

print(str1 + " " + str2)


# In[13]:


#repeat a string n-times

print(str1 * 3) #here, n = 3


# In[15]:


#String membership test

print('y' in str1) #here, y is in str1
print('a' in str1) #but here, a is not in str1


# In[16]:


#Lower function make the string in lower case

print(str1.lower())


# In[17]:


#Upper function make the string capitalize

print(str1.upper())


# In[56]:


#Split function break the strings into several parts using the paremeter

str3 = "this is a string for test"
str4 = str3.split(" ")
print(str4)


# In[57]:


#Join function merge all the elements of a list and make a string

str5 = ' '.join(str4)
print(str5)


# In[58]:


#find function return the first occurence of sub string

print(str5.find('is'))


# In[59]:


#replace function one part of string with other

print(str5.replace('is', 'was'))


# In[64]:


#sorting word of a string

print('Old str= ' + str3)

words = str3.split()
words.sort()

str4 = ' '.join(words)

print('New str= ' + str4)

