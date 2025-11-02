"""
Program: Sum of first n natural numbers
Description: Given n, print sum 1..n.

Example:
Input/Output:
n=10 -> 55
"""

n = int(input("Enter n value: "))
sum = 0
for i in range(1,n+1):
    sum +=i
print(sum)




