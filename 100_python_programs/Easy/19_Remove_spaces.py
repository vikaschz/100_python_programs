"""
Program: Remove spaces
Description: Remove all spaces from input string.

Example:
Input/Output:
'a b c' -> 'abc'
"""
s = input("Enter a string: ")
result = ""

for ch in s:
    if ch != " ":
        result += ch

print(result)
