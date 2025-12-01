"""
Program: Spiral Fill Matrix
Description: Fill NxN matrix in spiral order.

"""


N = int(input("Enter N: "))

# Create empty NxN matrix
matrix = [[0] * N for _ in range(N)]

top = 0
bottom = N - 1
left = 0
right = N - 1

num = 1  # start filling numbers

while left <= right and top <= bottom:

    # 1. Left → Right
    for i in range(left, right + 1):
        matrix[top][i] = num
        num += 1
    top += 1

    # 2. Top → Bottom
    for i in range(top, bottom + 1):
        matrix[i][right] = num
        num += 1
    right -= 1

    # 3. Right → Left
    if top <= bottom:
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1

    # 4. Bottom → Top
    if left <= right:
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

# Print the matrix
for row in matrix:
    print(*row)
