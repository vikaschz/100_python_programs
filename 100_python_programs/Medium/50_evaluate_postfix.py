"""
Program: Evaluate Postfix
Description: Evaluate postfix expression.
"""

stack = []
exp = input("Enter valid postfix expression: ")

for char in exp:
    if char.isnumeric():  # Operand
        stack.append(int(char))
    else:  # Operator
        b = stack.pop()
        a = stack.pop()

        if char == "+":
            stack.append(a + b)
        elif char == "-":
            stack.append(a - b)
        elif char == "*":
            stack.append(a * b)
        elif char == "/":
            stack.append(a / b)
        elif char == "%":
            stack.append(a % b)
        elif char == "^":
            stack.append(a ** b)

print("Result:", stack.pop())
