#!/usr/bin/env python
# coding: utf-8

# In[2]:


def getmax(b):
    return len(max(b,key=len))
a=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    e=input("Enter Element : ")
    a.append(e)
print("The length of longest word is :", getmax(a))    


# In[ ]:




