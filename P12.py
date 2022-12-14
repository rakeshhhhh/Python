#!/usr/bin/env python
# coding: utf-8

# In[6]:


n = int(input("Enter any number: "))
s = 0
for i in range(1, n):
    if(n % i == 0):
        s = s + i
if (s == n):
    print(n," is a Perfect number!")
else:
    print(n," is not a Perfect number!")


# In[ ]:




