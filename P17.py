#!/usr/bin/env python
# coding: utf-8

# In[4]:


def fibonacci(n):
    a = 0
    b = 1

    if n < 0:
        print("Incorrect input")
         
 
    elif n == 0:
        return 0
       
   
    elif n == 1:
        return b
    else:
        while a <= n:
            print(a)
            c = a + b
            a = b
            b = c
        
 
a=int(input("Enter The number you want to print fibonnaci series: "))
fibonacci(a)


# In[ ]:




