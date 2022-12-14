#!/usr/bin/env python
# coding: utf-8

# In[1]:


def palindrome(num):
    temp = num
    reverse = 0
    while temp > 0:
        remainder = temp % 10
        reverse = (reverse * 10) + remainder
        temp = temp // 10
    if num == reverse:
        print('Palindrome')
    else:
        print("Not Palindrome")

a=int(input("Enter a Number:"))
palindrome(a)


# In[ ]:




