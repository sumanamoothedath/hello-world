def add(a, b):
   return a + b

def subtract(a, b):
   return a - b

def multiply(a, b):
   return a * b

def divide(a, b):
   return a / b

print("Select operation as 1 for Add, 2 for Subtract,3 for Multiply and 4 for Divide")

choice = input("Enter choice(1,2,3 or 4):")

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")