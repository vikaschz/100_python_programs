"""
Program: Sum even numbers
Description: Sum only even numbers in a list.

Example:
Input/Output:
[1,2,3,4,5] -> 6
"""

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for i in l:
    if i%2==0:
        sum = sum + i
print(sum)





