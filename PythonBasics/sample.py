a = int(input("Enter the first number. \n"))
b = int(input("Enter the second number. \n"))
op = raw_input("Enter operator symbol. \n")
if(op=="+"):
    print("The sum of the numbers is", a+b)
elif(op=="-"):
    print("The total substraction is", a-b)
elif(op=="/"):
    print("The total division is", a/b)
elif(op=="*"):
    print("The multiplaction total is", a*b)
else:
    print("You have entered a wrong operator.\n")
    
    
    