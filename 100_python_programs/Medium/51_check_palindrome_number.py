"""
Program: Check Palindrome Number
Description: Check if number reads same backwards.

"""

num = int(input("Enter a number: "))
reverse = ""

temp = num

while temp > 0:
    digit = temp%10
    reverse += str(digit)
    temp = temp // 10

if int(reverse) == num:
    print(f"Number {num} is palindrome")
else:
    print(f"Number {num} is not a palindrome")





