"""
Program: Count words
Description: Count words in sentence.

Example:
Input/Output:
'This is fun' -> 3
"""
count = 0
s  = input("Enter: ").split()
for word in s:
    count += 1
print(count)