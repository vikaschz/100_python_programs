"""
Program: Palindrome String
Description: Check if string is palindrome (case-sensitive).
"""

string = input("Enter a string: ")
palindrome = ""
for i in range(len(string) - 1, -1, -1):
    palindrome += string[i]

if string == palindrome:

    print(f"{string} is palindrome")
else:
    print(f"{string} is not palindrome")
