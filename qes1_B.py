import math

try:
    num = int(input('Please Enter Your Number to calc the factorial: '))
    if num < 0:
        print("Your number is negative! Factorial is not defined for negative numbers.")
    else:
        f = math.factorial(num)
        print(f)
except ValueError:
    print("Please enter an integer.")
