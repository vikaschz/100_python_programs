"""
Program: Reverse the number
Difficulty: Easy
Description: print the reverse of a number
"""

num = int(input("Enter a number: "))

temp = num
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

print("Reversed:", rev)

