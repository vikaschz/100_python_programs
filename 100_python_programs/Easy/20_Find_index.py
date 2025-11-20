"""
Program: Find index
Description: Given list and item, print first index or -1.

Example:
Input/Output:
[3,5,2,9],2 -> 2
"""

l = [2, 3, 5, 7, 8, 9]

index = int(input("Enter a number: "))

pos = 0

for val in l:
    if val == index:
        print(f"index of {index} is: {pos}")
        break
    pos += 1
else:
    print("Value not found")
