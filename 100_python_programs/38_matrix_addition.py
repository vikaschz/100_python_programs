"""
Program: Matrix Addition
Description: Add two matrices of the same size.

Example:
Input:
Matrix 1:
1 2
3 4

Matrix 2:
5 6
7 8

Output:
Matrix Sum:
6 8
10 12
"""

def matrix_addition():
    # Get the number of rows and columns
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    # Initialize matrices
    matrix1 = []
    matrix2 = []
    result = []

    # Input for first matrix
    print("Enter elements for the first matrix:")
    for i in range(rows):
        row = []
        for j in range(cols):
            value = int(input(f"Enter element at position ({i+1}, {j+1}): "))
            row.append(value)
        matrix1.append(row)

    # Input for second matrix
    print("Enter elements for the second matrix:")
    for i in range(rows):
        row = []
        for j in range(cols):
            value = int(input(f"Enter element at position ({i+1}, {j+1}): "))
            row.append(value)
        matrix2.append(row)

    # Adding the two matrices
    for i in range(rows):
        row_sum = []
        for j in range(cols):
            row_sum.append(matrix1[i][j] + matrix2[i][j])
        result.append(row_sum)

    # Print the resulting matrix
    print("Resulting Matrix after Addition:")
    for row in result:
        print(row)

if __name__ == "__main__":
    matrix_addition()

