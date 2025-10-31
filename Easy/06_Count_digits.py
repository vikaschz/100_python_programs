"""
Program: Count digits
Difficulty: Easy
Description: Given an integer, print number of digits.
"""

def count_digits(n):
    count = 0
    while n > 0:
        n = n // 10      # Remove last digit
        count += 1       # Increase digit count
    return count

# Input
num = int(input("Enter a number: "))

# Edge case: if number is 0, it has 1 digit
if num == 0:
    print(1)
else:
    print(count_digits(num))
