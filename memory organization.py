
# coding: utf-8

# In[4]:

a=10
b=20
c=a
d=10


# In[5]:

print a


# In[6]:

print c


# In[7]:

a=100


# In[8]:

print a


# In[9]:

# mutable: list,dictionaries,arrays,dataframes
#immutable: int,float,complex,string,tuple


# In[10]:

a=10
b=20
c=a
d=10
print id(a),id(b),id(c),id(d)


# In[11]:

print a


# In[12]:

print c


# In[13]:

print d


# In[14]:

l1=[1,2,3,4]
l2=[5,6,7,8]
l3 = l1
l4=[1,2,3,4]
print id(l1),id(l2),id(l3),id(l4)


# In[15]:

a=100
c=200
d=400


# In[16]:

print id(a)


# In[17]:

print a,c,d


# In[18]:

l1


# In[19]:

l3


# In[20]:

l4


# In[21]:

l4.append(5)


# In[22]:

l4


# In[23]:

print id(l4)


# In[24]:

l1


# In[25]:

l1.append(6)


# In[26]:

l1


# In[27]:

l3


# In[28]:

l4


# In[29]:

print id(l1)


# In[30]:

d={1:2,3:4,5:6,77:8}


# In[31]:

d.has_key(3)


# In[32]:

print 3 in d.keys()


# In[33]:

a=10


# In[34]:

print type(a)


# In[35]:

c="python"
print type(c)


# In[36]:

a=10


# In[37]:

a="str123"


# In[38]:

a=10


# In[39]:

print a


# In[40]:

print type(a)


# In[41]:

a="str123"
print a
print type(a)


# In[42]:

a=[1,2,3,4,5]
print a
print type(a)


# In[43]:

import matplotlib.pyplot as plt
plt.plot([10,20,30,-4,5,6,7])
plt.show()


# In[44]:

import pandas as pd
data = pd.read_csv('data.csv')
print data.salary.mean()


# In[45]:

data[data['salary'] < data.salary.mean()]


# In[46]:

data.plot()
plt.show()


# In[49]:

a=10
b=20
c=30
print a+b
print a-b
print a*b
print "div=",a/b
print a%2
print a**2


# In[50]:

print 10/20


# In[51]:

print 10.0/20


# In[52]:

a=10
b=20
print a/b


# In[53]:

print a.0/b


# In[54]:

print float(a)


# In[55]:

print float(a/b) # 0 0.0 0.5 


# In[56]:

float(0)


# In[57]:

print float(a)/b


# In[58]:

float(a)


# In[59]:

print a,b


# In[60]:

print b/a


# In[61]:

print b/float(a)


# In[63]:

a+b


# In[64]:

a+"str1"


# In[ ]:



