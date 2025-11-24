"""
Program: Roman To Integer
Description: Convert Roman numerals to integer.

Hint:
- Scan using value rules.

"""

values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

number = input("Enter number in roman numerals: ")
result = 0
i = 0

while i < len(number):

    # Try 2-character match first
    if i + 1 < len(number) and number[i:i+2] in symbols:
        idx = symbols.index(number[i:i+2])
        result += values[idx]
        i += 2
    else:
        # single character
        idx = symbols.index(number[i])
        result += values[idx]
        i += 1

print(result)
