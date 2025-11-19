"""
Program: Rotate Matrix 90
Description: Rotate matrix 90° clockwise.
"""

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

# Input matrix
for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f"Enter element for ({i},{j}): "))
        row.append(value)
    matrix.append(row)

print("Matrix:")
for row in matrix:
    print(row)

# Step 1: Transpose of matrix
transpose = []
for i in range(len(matrix[0])):        # number of columns
    row = []
    for j in range(len(matrix)):       # number of rows
        row.append(matrix[j][i])
    transpose.append(row)

print("Transpose:")
for row in transpose:
    print(row)

# Step 2: Reverse each row to get 90° rotation
rotated = []
for row in transpose:
    rotated.append(row[::-1])

print("Matrix rotated 90° clockwise:")
for row in rotated:
    print(row)
