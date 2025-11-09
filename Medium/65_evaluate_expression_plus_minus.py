"""
Program: Evaluate Expression Plus Minus
Description: Evaluate + and - expression.
"""

expr = input("Enter expression: ")

# Remove spaces if any
expr = expr.replace(" ", "")

total = 0
current_num = ""
sign = 1   # +1 for plus, -1 for minus

for ch in expr:
    if ch.isdigit():
        current_num += ch
    else:
        total += sign * int(current_num)
        current_num = ""
        if ch == '+':
            sign = 1
        else:
            sign = -1

# Add the last number
total += sign * int(current_num)

print("Result:", total)
