"""
Program: Count vowels
Description: Count vowels (a,e,i,o,u) in a lowercase string.

Example:
Input/Output:
hello -> 2
"""
count = 0
vowels = "aeiou"
string = input("Enter a string: ").lower()

for ch in string:
    if ch in vowels:
        count = count + 1
print(count)

