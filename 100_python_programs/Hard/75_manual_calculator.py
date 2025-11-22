"""
Program: Manual Calculator
Description: Basic + and - calculator without eval.

"""

result = 0
token = "0"          # start empty
current_op = "+"    # previous operator

exp = input("Enter a valid expression: ").strip()

for ch in exp:

    # If digit, build the number
    if ch.isdigit():
        token += ch

    # If decimal point, add to token
    elif ch == ".":
        token += ch

    # If + or - operator
    elif ch == "+" or ch == "-":

        # Convert token to number
        number = float(token) if "." in token else int(token)

        # Apply previous operator
        if current_op == "+":
            result += number
        else:
            result -= number

        # Update current operator
        current_op = ch

        # Reset token
        token = ""

    else:
        print("Invalid expression")
        exit()  # stop program immediately

# Process last number
number = float(token) if "." in token else int(token)

if current_op == "+":
    result += number
else:
    result -= number

# Print result with 2 decimals
print(f"{result:.2f}")

