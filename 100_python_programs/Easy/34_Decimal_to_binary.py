"""
Program: Decimal to binary
Description: Convert decimal to binary string.

Example:
Input/Output:
13 -> 1101
"""

def D_to_B(b):
    if b == 0:
        return "0"
    temp = b
    B =""
    while temp>0:
        num = temp%2
        B += str(num)
        temp//=2
    return B[::-1]
        
decimal = int(input("Enter the Decimal number: "))
print(D_to_B(decimal))



