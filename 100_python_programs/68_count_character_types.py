"""
Program: Count Character Types
Description: Count uppercase, lowercase, digits, special characters.
"""

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"

count_Uppercase = 0
count_lowercase = 0
count_digits = 0
count_special_char = 0

s = input("Enter a string: ")

for char in s:
    if char in uppercase:
        count_Uppercase += 1
    elif char in lowercase:
        count_lowercase += 1
    elif char in digits:
        count_digits += 1
    else:
        count_special_char += 1

print(f"Uppercase: {count_Uppercase}")
print(f"Lowercase: {count_lowercase}")
print(f"Digits: {count_digits}")
print(f"Special characters: {count_special_char}")
