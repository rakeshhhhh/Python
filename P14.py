#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = int(input("Enterthe value of a: "))
b = int(input("Enter the value of b: "))

print("Prime numbers between", a, "and", b, "are:")

for num in range(a, b + 1):
 
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)


# In[ ]:




