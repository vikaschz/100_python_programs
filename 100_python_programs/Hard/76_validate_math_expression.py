"""
Program: Validate Math Expression
Description: Check if mathematical expression is valid.

Hint:
- Track parentheses, symbols.

"""
def is_valid_expression(expr):
    operators = "+-*/%^"
    digits = "0123456789"
    stack = []              # for parentheses
    prev = ""               # track previous non-space character
    decimal_allowed = True  # reset when a new number starts

    for ch in expr:
        if ch == " ":
            continue

        # ---------------- Parentheses ----------------
        if ch == "(":
            stack.append(ch)
            if prev in digits or prev == ")":
                return False
            prev = "("
            decimal_allowed = True

        elif ch == ")":
            if not stack:
                return False
            stack.pop()
            if prev in operators or prev == "(":
                return False
            prev = ")"
            decimal_allowed = True

        # ---------------- Digits ----------------
        elif ch in digits:
            prev = "digit"

        # ---------------- Decimal point ----------------
        elif ch == ".":
            if not decimal_allowed or prev not in ["digit"]:
                return False
            decimal_allowed = False
            prev = "digit"

        # ---------------- Operators ----------------
        elif ch in operators:
            # Cannot start with operator except unary + or -
            if prev == "" and ch not in "+-":
                return False

            # Two operators together → invalid
            if prev in operators or prev == "(":
                return False

            prev = ch
            decimal_allowed = True

        # ---------------- Invalid characters ----------------
        else:
            return False

    # ---------------- Final checks ----------------
    if stack:                 # Unmatched parentheses
        return False
    if prev in operators:     # Expression ends with operator
        return False

    return True


# ----------- MAIN -----------
expr = input("Enter a math expression: ")

if is_valid_expression(expr):
    print("Valid Expression")
else:
    print("Invalid Expression")

