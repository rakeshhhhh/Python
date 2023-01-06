#!/usr/bin/env python
# coding: utf-8

# In[14]:


try:
    fileptr = open("abc.txt","w")
    try: 
        fileptr.write("Hi I am good")
    finally:
        fileptr.close()
        print("file closed")
except:
    print("Error")


# In[ ]:





# In[ ]:




