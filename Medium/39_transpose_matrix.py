"""
Program: Transpose Matrix
Description: Print matrix transpose.

Example:
Input:
Matrix:
1 2 3
4 5 6

Output:
Transpose:
1 4
2 5
3 6
"""

def transpose_matrix():
    # Get the number of rows and columns
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    # Initialize the matrix
    matrix = []

    # Input for the matrix
    print("Enter elements for the matrix:")
    for i in range(rows):
        row = []
        for j in range(cols):
            value = int(input(f"Enter element at position ({i+1}, {j+1}): "))
            row.append(value)
        matrix.append(row)

    # Transposing the matrix
    transposed = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)

    # Print the transposed matrix
    print("Transposed Matrix:")
    for row in transposed:
        print(row)

if __name__ == "__main__":
    transpose_matrix()





