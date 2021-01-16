import sys

try:
    x=int(input("Insert value of x: "))
    y=int(input("Insert value of y: "))
except ValueError:
    print("Invalid imput!")
sys.exit(1)    

try:
    result=x/y
except ZeroDivisionError:
    print("Error! You can't divide by zero.")
sys.exit(1)

print(result)