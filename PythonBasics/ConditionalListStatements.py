list = ["Larry", "curly", "Moe"]
numlist =[1,2,3, ]

#If one value is one list
if "curly" in list:
    print("Yay, curry in list")

#If one value is one list
if 2 in numlist:
     print("Yay, 2 in num list")

#If two values are the same list
if "curly" and "Larry" in list:
    print("Yay, curly and larry in list")

a = list + numlist
if "curly" and 2 in a:
    print("Yay, curly and 2 are in the two lists")