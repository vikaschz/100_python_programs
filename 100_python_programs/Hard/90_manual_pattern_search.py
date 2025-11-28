"""
Program: Manual Pattern Search
Description: Find all substring occurrences (no find).

Hint:
- Sliding loop.

"""
s = input("Enter a string: ")
pat = input("Enter a sub string: ")

n = len(s)
m = len(pat)

found = False

for i in range(n - m + 1):       # slide window
    if s[i:i+m] == pat:          # check substring match
        print(f"Substring found at index {i}")
        found = True

if not found:
    print("Substring not found")

