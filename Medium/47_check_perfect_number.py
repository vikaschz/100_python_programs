"""
Program: Check Perfect Number
Description: Check if number is perfect.

"""

n = int(input("Enter number: "))
sum = 0

for num in range(1, (n // 2) +1):
    if n % num == 0:
        sum = sum + num

if sum == n:
    print(f"{n} is a Perfect Number")
else:
    print(f"{n} is Not a Perfect Number")
