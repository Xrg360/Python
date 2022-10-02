#this program is to display a menu driven calculator
from secrets import choice


def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b
def mod(a, b):
    return a % b
def exp(a, b):
    return a ** b
def floordiv(a, b):
    return a // b

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Modulus\n6. Exponent\n7. Floor Division\n8. Exit\n")

ch= int(input("Enter your choice: "))
while(ch != 8):
    if ch == 1:
    
        print("The sum is: ", add(a, b))
    elif ch == 2:
                
        print("The difference is: ", sub(a, b))
    elif ch == 3:
                
        print("The product is: ", mul(a, b))
    elif ch == 4:
                
        print("The quotient is: ", div(a, b))
    elif ch == 5:
                
        print("The remainder is: ", mod(a, b))
    elif ch == 6:
                
        print("The result is: ", exp(a, b))
    elif ch == 7:
                
        print("The result is: ", floordiv(a, b))
    elif ch == 8:
        print("Thank you for using the calculator")
        break
    else:
        print("Invalid choice")
