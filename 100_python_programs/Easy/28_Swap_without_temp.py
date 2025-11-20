"""
Program: Swap without temp
Description: Swap two numbers without temp.

Example:
Input/Output:
4 9 -> 9 4
"""

a = int(input("Enter A: "))
b = int(input("Enter B: "))
print(f"Before swapping\nA = {a}\nB = {b}")
a,b = b,a
print(f"After swapping\nA = {a}\nB = {b}")

