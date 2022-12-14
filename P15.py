#!/usr/bin/env python
# coding: utf-8

# In[5]:


def bitodec(bi):
    dec = 0
    i = 1
    while bi!=0:
        rem = bi%10
        dec = dec + (rem*i)
        i = i*2
        bi = int(bi/10)
    return dec
print("Enter the Binary Number: ")
bi = int(input())
b=bitodec(bi)
print("Equivalent Decimal Value = ", b)


# In[ ]:




