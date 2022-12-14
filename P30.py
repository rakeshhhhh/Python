#!/usr/bin/env python
# coding: utf-8

# In[3]:


string = input("Enter a String : ")  
count = 0  
for i in range(0, len(string)):
    if(string[i] != ' '):
        count = count + 1  
print("Total number of characters in a string: " + str(count)) 


# In[ ]:




