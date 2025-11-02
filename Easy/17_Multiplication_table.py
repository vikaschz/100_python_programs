"""
Program: Multiplication table
Difficulty: Easy
Description: Print multiplication table of n up to 10.

Example:
Input/Output:
n=3 -> 3x10=30
"""

n = int(input("Enter n value: "))

for i in range(1,11):
    print(f"{n} x {i} = {n*i}")



