import re

a =input("enter the phone number:")

if(re.search("[\d]{10}",a) and len(a)==10):
    print("this is correct number:" ,a)
else:
    print("this is not correct number:" ,a)

str1 = input("enter emailid: ")

if(re.search("[\w,.$&]{6,30}@[\w,.]{19}",str1)):
    print("this is valid emailid:" ,str1)
else:
    print("this is not valid emailid:" ,str1)

str2 = input("enter ip address")

if(re.search("[\d,.]{4}[\d,.]{4}[\d,.]{4}[\d,.]",str2)):
    print("this is valid ip:" ,str2)

else:
    print("this is not valid ip address",str2)