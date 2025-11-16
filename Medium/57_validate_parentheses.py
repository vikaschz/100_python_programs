"""
Program: Validate Parentheses
Description: Check balanced parentheses.

"""

stack = []
p = input("Enter parentheses: ")

for ch in p:

    # Opening brackets
    if ch in "({[":
        stack.append(ch)

    # Closing brackets
    elif ch in ")}]":

        # If stack empty → no matching opening
        if not stack:
            print("Not balanced")
            break

        top = stack[-1]

        # Matching pairs
        if (ch == ")" and top == "(") or \
           (ch == "}" and top == "{") or \
           (ch == "]" and top == "["):
            stack.pop()
        else:
            print("Not balanced")
            break

else:
    # Loop completed normally
    if not stack:
        print("Balanced")
    else:
        print("Not balanced")
