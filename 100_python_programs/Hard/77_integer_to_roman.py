"""
Program: Integer To Roman
Description: Convert integer to Roman numerals.

Hint:
- Use mapping and subtractive logic.

"""
def int_to_roman(num):
    values = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4, 1
    ]

    symbols = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV", "I"
    ]

    result = ""

    # Loop through each value-symbol pair
    for i in range(len(values)):
        while num >= values[i]:
            result += symbols[i]
            num -= values[i]

    return result


# Example
number = int(input("Enter an integer: "))
print("Roman Numeral:", int_to_roman(number))
