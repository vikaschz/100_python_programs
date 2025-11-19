"""
Program: sum of the digits
Difficulty: Easy
Description: Sum all digits of the integer.
"""

num = int(input("Enter a number: "))

temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit
    temp //= 10

print(f"Sum of {num} is : {sum}")
