"""
Program: string difference
Description: Compare two strings (diff).
"""

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

i = 0
n1 = len(s1)
n2 = len(s2)

while i < n1 and i < n2:
    if s1[i] != s2[i]:
        print(f"Position {i}: '{s1[i]}' → '{s2[i]}'  (changed)")
    i += 1

# Remaining characters (if lengths differ)
if n1 < n2:
    # extra chars in s2 = insertion
    for j in range(i, n2):
        print(f"Position {j}: insertion of '{s2[j]}'")

elif n1 > n2:
    # missing chars in s2 = deletion
    for j in range(i, n1):
        print(f"Position {j}: deletion of '{s1[j]}'")
