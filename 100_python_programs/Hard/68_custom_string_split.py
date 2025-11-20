"""
Program: Custom String Split
Description: Implement a custom split function (no .split).

Hint:
- Iterate manually and detect word boundaries.

"""
text = input("Enter a string: ")

result = []

current_word = ""
for char in text:
    if char != " ":
        current_word += char
    else:
        if current_word != "":      # FIX: avoid empty words
            result.append(current_word)
        current_word = ""

if current_word != "":
    result.append(current_word)
print(result)


