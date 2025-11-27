"""
Program: Extract Numbers
Description: Extract all numbers from string, incl decimals.

Hint:
- Scan char-by-char.
"""

s = input("Enter a string: ")

numbers = []
current = ""

for ch in s:
    if ch.isdigit() or ch == ".":      # part of number
        current += ch
    else:
        if current != "":              # number ended
            numbers.append(current)
            current = ""

# if number ends at last character
if current != "":
    numbers.append(current)

print(numbers)
