#!/usr/bin/env python
# coding: utf-8

# In[1]:


def fact(n):
    if (n==1 or n==0):
        return 1
    else:
        return (n*fact(n - 1))
 
num = int(input("Enter a number: "));
print("Factorial Of ",num," : ",fact(num))


# In[ ]:




