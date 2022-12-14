
a = input("Enter a String")
print("The original string is : " + str(a))
K = '$'
res = a[0] + a[1:].replace(a[0], K)
print("Replaced String : " + str(res))
