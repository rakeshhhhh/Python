#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cmath
a=int(input("Enter The Number : "))
b=int(input("Enter The Number : "))
c=int(input("Enter The Number : "))
d=(b**2)-(4*a*c)
sol1=(-b+(cmath.sqrt(d)))/(2*a)
sol2=(-b-(cmath.sqrt(d)))/(2*a)
print("The solution of quadratic equation are {} and {} ".format(sol1,sol2))


# In[ ]:




