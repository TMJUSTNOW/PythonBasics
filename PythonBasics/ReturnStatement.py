# Advanced function with a statement
def Order(item):
    if(item == "Chicken"):
        return 1
    else:
        return 2

itemname = input("Enter the item name.\n")
result  = Order(itemname)
print("Result is", result)
if(result==1):
    print("5$. Thank you for shopping. ")
 