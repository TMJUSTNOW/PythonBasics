#Advanced default argument with manual changes allowable

a = int(input("Enter quantity of itmens you want to check out. \n"))
if(a == 0):
    a = 1
else:
    a = a

def Order(a):
    print("Price is", a * 40, "$")

Order(a)