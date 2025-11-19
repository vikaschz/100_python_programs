"""
Program: Maximum of Three Numbers
Difficulty: Easy
Description: Given three numbers, print the maximum.
Example:
Input: 3 9 7
Output: 9
"""

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)
