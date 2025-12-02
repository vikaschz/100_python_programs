"""
Program: Case Sensitive Compression
Description: Compress with case sensitivity.

Hint:
- Count consecutive runs.

"""

s = input("Enter a string: ")

if not s:
    print("")
    exit()

result = ""
prev = s[0]
count = 1

for ch in s[1:]:
    if ch == prev:
        count += 1
    else:
        result += prev + str(count)
        prev = ch
        count = 1

result += prev + str(count)

print(result)
