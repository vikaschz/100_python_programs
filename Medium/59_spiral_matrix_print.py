"""
Program: Spiral Matrix Print
Description: Print matrix in spiral order.
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

print("Spiral Matrix:")

top = 0
bottom = rows - 1
left = 0
right = cols - 1

while top <= bottom and left <= right:

    # Print top row (left → right)
    for i in range(left, right + 1):
        print(matrix[top][i], end=" ")
    top += 1

    # Print right column (top → bottom)
    for i in range(top, bottom + 1):
        print(matrix[i][right], end=" ")
    right -= 1

    # Print bottom row (right → left)
    if top <= bottom:
        for i in range(right, left - 1, -1):
            print(matrix[bottom][i], end=" ")
        bottom -= 1

    # Print left column (bottom → top)
    if left <= right:
        for i in range(bottom, top - 1, -1):
            print(matrix[i][left], end=" ")
        left += 1
