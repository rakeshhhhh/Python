#!/usr/bin/env python
# coding: utf-8

# In[2]:


a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
print("OPERATIONS")
print("------------")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
c=input("Enter the choice(1-4):")
if c=='1':
    d=a+b
    print(a,"+",b,"=",d)
elif c=='2':
    d=a-b
    print(a,"-",b,"=",d)
elif c=='3':
    d=a*b
    print(a,"*",b,"=",d)
elif c=='4':
    d=a/b
    print(a,"/",b,"=",d)
else:
    print("Invalid Choice")
    
    


# In[ ]:





# In[ ]:




