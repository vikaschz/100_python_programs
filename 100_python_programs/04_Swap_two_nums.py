"""
Program: Swap Two Numbers
Description: Given two numbers A and B, output them swapped.

Example:
Input: A=3 B=8
Output: A=8 B=3
"""

a = int(input("Enter A: "))
b = int(input("Enter B: "))
print(f"Before swapping\nA = {a}\nB = {b}")
a,b = b,a
print(f"After swapping\nA = {a}\nB = {b}")
    
