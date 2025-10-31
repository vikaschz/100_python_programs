"""
Program: sum of the digits
Difficulty: Easy
Description: Sum all digits of the integer.
"""


def sum_of_digits(n):
    temp = n
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum += digit
        temp //= 10

    return f"Sum of {n} is : {sum}"


num = int(input("Enter a number: "))
print(sum_of_digits(num))
