
# coding: utf-8

# In[2]:


"""Function breakdown a program into smaller and moduler chunk"""

def messagePrinter(message):
    """This function just print a message. The parameter is the user message and return value is nothing"""
    print('The custorm message is: ' + message)
    
messagePrinter('Beachtung! Türen werden automatisch geöffnet')


# In[6]:


#function with return type

def getSum(data):
    """This function calculate the summation of a give list and returns it sum value"""
    _sum = 0
    
    for element in data:
        _sum += element
    return _sum

myData = [1, 3, 5, 2, 4]
summation = getSum(myData)

print(getSum.__doc__) #we can print the function desxription comment using __doc__
print(summation)


# In[7]:


"""There are two types of functions: Standrad library function and user define function. Here are some STD Functions"""

#abs function return the absolute value of a function

n = -100
print(abs(n))


# In[8]:


#dir function returns all the attributes and functions of a data object

arr = []
print(dir(arr))


# In[9]:


#divmod function takes parameters(d1, d2) and return a tuple(q, m) where d1=divident, d2=divisor, q=quotient & m=modules

dm = divmod(7, 2)
print(dm)


# In[18]:


#enumerate function

data = [10, 20, 30, 40, 50]

ind = [i for i,val in enumerate(data)]

print(ind)


# In[24]:


#filter function take two paremeter one is the custom function we use and another one is the sequence

def positiveFilter(num):
    """This function remove all the negative numbers from a list"""
    
    if num > 0:
        return num

numbers = range(-10, 10)
print(list(numbers))

pos_num = list(filter(positiveFilter, numbers))
print(pos_num)


# In[3]:


#Map function is used to do any action over the list

def squareMaker(num):
    return num ** 2

numbers = [1, 2, 3, 4, 5]

squares = list(map(squareMaker, numbers))

print(squares)


# In[5]:


#Reduce function apply the action in consequence elements in a list

def multiplicationFunction(x, y):
    return x * y

from functools import reduce

numbers = [1, 2, 3, 4, 5]

mulOutput = reduce(multiplicationFunction, numbers)

print(mulOutput)


# In[7]:


#Default Arguments

def printer(name, message="No message found"):
    print('Hello ' + name + ' Your message: ' + message)
    return;

#call by using two arguments
printer('Jaber', 'How are you?')

#call by using one argument
printer('Arif')


# In[9]:


#Keyword Arguments: Allow to pass variable length of arguments

def printer1(**kwargs):
    if kwargs:
        print('Hello ' + kwargs['name'] + '. Your message: ' + kwargs['message'])
    return;

printer1(name = 'Pream', message='How are you?')


# In[10]:


#Arbitary Arguments

def printer3(*names):
    for name in names:
        print(name)
    return;

printer3('Mahfuz', 'Azhar', 'Foysol', 'Maha')


# In[15]:


#Recursion

def factorial(n):
    return 1 if n==1 else (n * factorial(n-1))

n = 5
print('factorial of {} is = {}'.format(n, factorial(n)))


# In[22]:


#Lambda Function

square = lambda x: x**2 
#here, square is the name of the function, x is input and x**2 is the return statement

numbers = [1, 2, 3, 4, 5]

squareNumber = list(map(square, numbers)) #here, I pass the name of the lambda function
print(squareNumber)

cubeNumber = list(map(lambda x: x**3, numbers)) #here, I write the lambda expression in the map function
print(cubeNumber)

