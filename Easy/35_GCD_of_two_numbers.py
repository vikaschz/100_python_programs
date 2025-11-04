"""
Program: GCD of two numbers
Difficulty: Easy
Description: Compute GCD of two integers.

Example:
Input/Output:
12 18 -> 6
"""

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a < 0 or b < 0:
    print("Please enter positive numbers.")
else:
    
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a

    print("GCD =", a)
