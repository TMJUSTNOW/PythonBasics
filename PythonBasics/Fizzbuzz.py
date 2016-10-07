#Implementing the simple fizzbuzz in python..
for i in range(0, 101) :
    a = i % 3 == 0
    b = i % 5 == 0

    if(a & b):
        print("FizzBuzz")
    elif(a):
        print("Fizz")
    elif(b):
        print("Buzz")
    else:
        print(i)
        

