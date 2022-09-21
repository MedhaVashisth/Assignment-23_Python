#!/usr/bin/env python
# coding: utf-8

# In[1]:


def func(a,b=6,c=8):
    print(a,b,c)
    


# In[2]:


func(1,2)


# In[3]:


def func(a,b,c=5):
    print(a,b,c)
    


# In[4]:


func(1,c=3,b=2)


# In[5]:


def func(a,**kargs):
    print(a,kargs)
    


# In[6]:


func(1,c=3,b=2)


# In[7]:


def func(a,b,c=8,d=5):
    print(a,b,c,d)


# In[9]:


func(1,*(5,6))


# In[10]:


def func(a,b,c):a=2;b[0]='x';c['a']='y'


# In[12]:


l=1;m=[1];n={'a':0}


# In[13]:


func(l,m,n)


# In[15]:


l,m,n


# In[ ]:




