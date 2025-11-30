"""
Program: Repeated Words Positions
Description: Find repeated words with positions.

Hint:
- Track indexes of words.

"""


s = input("Enter a string: ")
pat = input("Enter pattern to search: ")

n = len(s)
m = len(pat)

found = False

for i in range(n - m + 1):
    if s[i:i+m] == pat:
        print(f"Substring found at index {i}")
        found = True

if not found:
    print("Substring not found")
