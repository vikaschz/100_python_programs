"""
Program: Fibonacci Series
Description: Print first n Fibonacci numbers.

"""

n = int(input("Enter n term: "))
a, b = 0, 1
for _ in range(max(0, n)):
    print(a, end=" ")
    a, b = b, a + b
print()



