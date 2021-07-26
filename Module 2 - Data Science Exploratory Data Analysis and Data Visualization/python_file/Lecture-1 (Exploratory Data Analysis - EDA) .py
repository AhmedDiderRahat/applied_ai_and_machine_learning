
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from statsmodels import robust as rb
from scipy import stats as st


# In[2]:


iris = pd.read_csv("iris.csv")


# In[3]:


#get data-points and feature

print(iris.shape)


# In[4]:


#get the column name

print(iris.columns)


# In[5]:


#get the number of specis with respect to different class

'''Iris data set is a balance data set. See, balance Vs imbalanace dataset'''

iris["species"].value_counts()


# ### <u> 2-D scatter plot:</u>

# In[6]:


iris.plot(kind="scatter", x="sepal_length", y="sepal_width")
plt.show()


# In[7]:


sb.set_style("whitegrid")
sb.FacetGrid(iris, hue="species", size=4).map(plt.scatter, "sepal_length", "sepal_width").add_legend();

plt.show()


# Observation(s):
# 
# 1. Using sepal_length and sepal_width features, we can distinguish Setosa flowers from others.
# 2. Seperating Versicolor from Viginica is much harder as they have considerable overlap.

# ### <u>Pair Plots:

# In[8]:


plt.close();

sb.set_style("whitegrid")
sb.pairplot(iris, hue="species", size=3);

plt.show();


# <b>Observations:</b>
# 
# 1. petal_length and petal_width are the most useful features to identify various flower types.
# 2. While Setosa can be easily identified (linearly seperable), Virnica and Versicolor have some overlap (almost linearly seperable).
# 3. We can find "lines" and "if-else" conditions to build a simple model to classify the flower types.

# ### <u>Histogram:<u>

# In[9]:


sb.FacetGrid(iris, hue="species", size=5)    .map(sb.distplot, "petal_length")    .add_legend();
plt.show();


# ### <u>PDF and CDF:<u>

# In[10]:


iris_setosa = iris.loc[iris["species"] == "setosa"];

counts, bin_edge = np.histogram(iris_setosa['petal_length'], bins=10, density=True)

pdf = counts / sum(counts)

np.set_printoptions(formatter={'float': '{: 0.3f}'.format})
print('COUNT= ', counts)
np.set_printoptions(None)

print('EDGE=  ', bin_edge)
print('\nPDF=   ', pdf)

#calculate CDF

cdf = np.cumsum(pdf)

print('\nCDF=   ', cdf)


plt.plot(bin_edge[1:], pdf)
plt.plot(bin_edge[1:], cdf)


# ### <u>Mean, Median, Mode:<u>

# In[11]:


#For iris-setosa

print('Mean= ', np.mean(iris_setosa['petal_length']))
print('Median= ', np.median(iris_setosa['petal_length']))
print('Mode= ', st.mode(iris_setosa['petal_length']))


# ### <u>Standard Deviation:<u>

# In[12]:


print('SD= ', np.std(iris_setosa['petal_length']))


# ### <u>Percentiles and Quintiles:<u>

# <j>A percentile (or a centile) is a measure used in statistics indicating the value below which a given percentage of observations in a group of observations fall. For example, the 20th percentile is the value (or score) below which 20% of the observations may be found.
# 
# <b>Quartiles</b> are specific types of <b>percentile</b>. The 25th percentile is also known as the <b>first quartile (Q1)</b>, the 50th percentile as the <b>median or second quartile (Q2)</b> , and the 75th percentile as the <b>third quartile (Q3)</b>.

# In[13]:


print('20 % of Setosa has petal length of ' + str(np.percentile(iris_setosa['petal_length'], 20)) + ' or lower')
print('90 % of Setosa has petal length of ' + str(np.percentile(iris_setosa['petal_length'], 90)) + ' or lower')


# In[14]:


q1, q2, q3 = np.percentile(iris_setosa['petal_length'], [25, 50, 75])

print('1st Quentile (Q1) = ', q1)
print('2nd Quentile (Q2) = ', q2)
print('3rd Quentile (Q3) = ', q3)


# ### <u>Median Absolute Deviation (MAD):<u>

# The median absolute deviation(MAD) is a robust measure of how spread out a set of data is. The variance and standard deviation are also measures of spread, but they are more affected by extremely high or extremely low values and non normality. If your data is normal, the standard deviation is usually the best choice for assessing spread. However, if your data isn’t normal, the MAD is one statistic you can use instead.
# 
# if X<sub>1</sub>, X<sub>2</sub>, X<sub>3</sub>,...., X<sub>n</sub> dataset MAD is define as: MAD = Median( |X<sub>m</sub> - X<sub>i</sub>| ) [Where, X<sub>m</sub> = Median(X<sub>i</sub>)and i=1,2,3,...,n]
# 
# For example, Consider the data (1, 1, 2, 2, 4, 6, 9). It has a median value of 2. The absolute deviations about 2 are (1, 1, 0, 0, 2, 4, 7) which in turn have a median value of 1 (because the sorted absolute deviations are (0, 0, 1, 1, 2, 4, 7)). So the median absolute deviation for this data is 1.

# In[15]:


print('Using library= ', rb.mad(iris_setosa['petal_length']))

print('Using Calculation= ', np.median(np.absolute(np.median(iris_setosa['petal_length'])-iris_setosa['petal_length'])))


# <b>rb.mad()</b> function is not working properly as it calculate the mad with Gaussian districbution. 

# ### <u>Interquartile Range (IQR):<u>

# The interquartile range (IQR), also called the <b>midspread</b>, <b>middle 50%</b>, or <b>H‑spread</b>, is a measure of statistical dispersion, being equal to the difference between 75<sup>th</sup> and 25<sup>th</sup> percentiles, or between upper and lower quartiles. <br>So,IQR = Q<sub>3</sub> −  Q<sub>1</sub>.

# In[16]:


print('IQR of setosa petal length= ',st.iqr(iris_setosa['petal_length']))


# ### <u>Box Plot:<u>

# A box plot is a type of chart often used in explanatory data analysis. Box plots visually show the distribution of numerical data and skewness through displaying the data quartiles (or percentiles) and averages. 
# <img src="boxplot.png" alt="Box Plot" style="float: bottom; height:250px; width:350px"/>

# In[17]:


sb.boxplot(x='species', y='petal_length', data=iris)


# ### <u>Violin Plot:<u>

# A violin plot is a method of plotting numeric data. It is similar to a box plot, with the addition of a rotated kernel density plot on each side. Violin plots are similar to box plots, except that they also show the probability density of the data at different values, usually smoothed by a kernel density estimator. 
# <img src="violin_plot.png" alt="Box Plot" style="float: bottom; height:300px; width:450px"/>

# In[18]:


sb.violinplot(x="species", y="petal_length", data=iris, size=8)
plt.show()


# ### <u>Multivariate probability density, contour plot:</u>

# In[19]:


sb.jointplot(x="petal_length", y="petal_width", data=iris_setosa, kind="kde");
plt.show();

