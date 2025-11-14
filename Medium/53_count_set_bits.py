"""
Program: Count Set Bits
Description: Count 1s using bitwise AND and right shift.
"""

n = int(input("Enter a number: "))
count = 0
temp = n

while temp > 0:
    if temp & 1:     
        count += 1
    temp = temp >> 1  
print(f"Number of set bits in {n} is: {count}")

