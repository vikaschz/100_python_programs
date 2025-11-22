"""
Program: Expression Tokenizer
Description: Convert math expression to tokens.

Hint:
- Separate numbers, operators, parentheses.

"""

tokens = []
# example input = 3.2 + (10 - 4)*5
exp = input("Enter valid expression: ")

buffer = ""
num = "0123456789"
operators = ["+", "-", "*", "/", "%", "^"]
for ch in exp:
    if ch in num or ch == ".":
        buffer += ch
    elif ch in operators:
        if buffer != "":
            tokens.append(buffer)
            buffer = ""
        tokens.append(ch)
    elif ch in ["(", ")"]:
        if buffer != "":
            tokens.append(buffer)
            buffer = ""
        tokens.append(ch)

    elif ch == " ":
        if buffer != "":
            tokens.append(buffer)
            buffer = ""

tokens.append(buffer)
print(tokens)



