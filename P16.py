#!/usr/bin/env python
# coding: utf-8

# In[3]:


def sum1(n):
    s = 0
    while(n > 0):
        s+=n
        n=n-1
    return s
    
a=int(input("Enter The limit : "))    
b=sum1(a)
print("The sum is: ",b)
    


# In[ ]:




