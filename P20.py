#!/usr/bin/env python
# coding: utf-8

# In[2]:


def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

print("M E N U ")
print("--------- ")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1-4):")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2':
        print(num1, "-", num2, "=", sub(num1, num2))
    elif choice == '3':
        print(num1, "*", num2, "=", mul(num1, num2))
    elif choice == '4':
        print(num1, "/", num2, "=", div(num1, num2))
    else:
        print("Invalid Input")
    x = input("Do You want to Continue? (Yes/No): ")
    if x == "n":
        break


# In[ ]:




