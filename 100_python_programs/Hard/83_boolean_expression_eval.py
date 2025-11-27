"""
Program: Boolean Expression Eval
Description: Evaluate boolean expression (AND/OR).
"""

expr = input("Enter boolean expression (e.g., True AND False): ")

# Split into 3 parts
a, op, b = expr.split()

# Convert input to boolean values
def to_bool(x):
    if x.lower() in ["true", "1", "yes"]:
        return True
    else:
        return False

A = to_bool(a)
B = to_bool(b)

# Evaluate
if op.upper() == "AND":
    result = A and B
elif op.upper() == "OR":
    result = A or B
else:
    result = "Invalid operator"

print("Result:", result)
