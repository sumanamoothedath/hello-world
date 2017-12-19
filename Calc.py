#!/usr/bin/env python

def add(a, b):
    """Adds a and b and returns the sum."""
    return(a + b)

def subtract(a, b):
    """Subtracts a and b and returns the difference."""
    return a - b

def multiply(a, b):
    """Multiplies a and b and returns the product."""
    return a * b

def divide(a, b):
    """Divides a and b and returns the quotient."""
    return a / b

if __name__ == "__main__":
   print("Select operation as 1 for Add, 2 for Subtract,3 for Multiply and 4 for Divide")
choice =input("Enter choice(1,2,3 or 4):")
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

if choice == '1':
   print('{} + {} = '.format(num1, num2))
   print(add(num1,num2))

elif choice == '2':
    print('{} - {} = '.format(num1, num2))
    print(subtract(num1,num2))

elif choice == '3':
    print('{} * {} = '.format(num1, num2))
    print(multiply(num1,num2))

elif choice == '4':
    print('{} / {} = '.format(num1, num2))
    print(divide(num1,num2))
else:
   print("Invalid input")
