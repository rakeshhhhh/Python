#!/usr/bin/env python
# coding: utf-8

# In[2]:


def power(n,p):
    if(p==1):
        return(n)
    if(p!=1):
        return(n*power(n,p-1))
n=int(input("Enter Number: "))
p=int(input("Enter Power value: "))
print("Result:",power(n,p))


# In[ ]:




