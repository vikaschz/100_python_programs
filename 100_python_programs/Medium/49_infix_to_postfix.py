"""
Program: Infix To Postfix
Description: Convert infix to postfix.
"""

stack = []
postfix = ""
priority = {"+": 1, "-": 1, "*": 2, "/": 2, "%": 2, "^": 3}

exp = input("Enter valid infix expression: ")

for char in exp:
    if char.isalpha():  # Operand
        postfix += char

    elif char == "(":  # Left bracket
        stack.append(char)

    elif char == ")":  # Right bracket → pop until '('
        while stack and stack[-1] != "(":
            postfix += stack.pop()
        stack.pop()  # Remove '('

    else:  # Operator
        while stack and stack[-1] != "(" and priority[stack[-1]] >= priority[char]:
            postfix += stack.pop()
        stack.append(char)

# Pop remaining operators
while stack:
    postfix += stack.pop()

print("Postfix:", postfix)
