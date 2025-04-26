# addition
def add(x, y):
    return x + y
#subtraction
def sub(x, y):
    return x - y
#multiplication
def mul(x, y):
    return x * y
#division
def div(x, y):
    if(y==0):
        return "Error Division by zero not allowed"
    else:
        return x / y

def calculator():
    print("select operation")
    print("1.ADDITION")
    print("2.SUBTRACTION")
    print("3.MULTIPLICATION")
    print("4.DIVISION")

    while True:
    # taking input from the users
        choice=input("Enter the choices (1/2/3/4)")
    # check if the input is one of the four options
        if choice in ['1','2','3','4']:
            num1=float(input("Enter first number"))
            num2=float(input("Enter second number"))
            
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1,num2)}")
            if choice == '2':
                print(f"{num1} - {num2} = {sub(num1,num2)}")
            if choice == '3':
                print(f"{num1} * {num2} = {mul(num1,num2)}")
            if choice == '4':
                print(f"{num1} / {num2} = {div(num1,num2)}")
            
     # option to exit the loop
        next_calculation = input("Do you want to perform another operation ? yes/no")
        if next_calculation.lower() != 'yes':  
            break
    print("exiting calculator . Good bye")

    # call the calculator function 
calculator()

