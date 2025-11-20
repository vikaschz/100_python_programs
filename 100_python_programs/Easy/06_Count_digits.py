"""
Program: Count digits
Difficulty: Easy
Description: Given an integer, print number of digits.
"""


n = int(input("Enter a number: "))
count = 0
while n > 0:
    n = n // 10     
    count += 1       
print(count)
