"""
Program: Compressed String Expansion
Description: Expand compressed strings.

Hint:
- Repeat characters based on count.

"""

s = input("Enter a string: ")
res = ""
prev = ""
num = ""

for ch in s:
    if ch.isalpha():
        if prev and num:
            res += prev * int(num)
        prev = ch
        num = ""
    else:
        num += ch

# Add the last group
if prev and num:
    res += prev * int(num)

print(res)
