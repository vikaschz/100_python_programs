"""
Program: Sum Of Diagonals
Description: Sum primary and secondary diagonals.

Hint:
- Loop indexes carefully avoid double-center.

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

primary_diagonal = 0
secondary_diagonal = 0

for i in range(len(matrix)):
    primary_diagonal += (matrix[i][i])

for j in range(len(matrix)):
    secondary_diagonal += (matrix[j][cols - 1 - j])

print(f"The sum of primary diagonal is: {primary_diagonal}")
print(f"The sum of secondary diagonal is: {secondary_diagonal}")
if rows == cols and rows % 2 != 0:
    center = matrix[rows // 2][cols // 2]
    print(f"The sum of both diagonals is: {primary_diagonal + secondary_diagonal - center}")
else:
    print(f"The sum of both diagonals is: {primary_diagonal + secondary_diagonal}")