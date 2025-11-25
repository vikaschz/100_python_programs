"""
Program: Snake Case Converter
Description: Convert sentence to snake_case manually.

Hint:
- Lowercase and join with underscores.

"""

s = input("Enter a sentence: ").lower()

result = ""
prev_underscore = False

for ch in s:
    if ch.isalnum():          # letters or numbers
        result += ch
        prev_underscore = False
    else:
        if not prev_underscore:
            result += "_"
            prev_underscore = True

print(result)
