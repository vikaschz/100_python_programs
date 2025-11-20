"""
Program: Binary to Decimal
Description: Convert binary string to decimal.

Example:
Input/Output:
1011 -> 11
"""

binary = input("Enter number in binary: ")

decimal = 0
length = len(binary)

for i in range(length):
    digit = int(binary[i])          
    power = length - i - 1          
    decimal += digit * (2 ** power) 

print(decimal)

