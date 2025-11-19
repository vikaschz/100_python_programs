"""
Program: Check armstrong 3digit
Description: Check if 3-digit number is Armstrong.

Example:
Input/Output:
153 -> Armstrong
"""


n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Negative numbers are not considered Armstrong numbers.")
else:
    # handle 0 correctly
    if n == 0:
        digits = 1
    else:
        # count digits
        temp = n
        digits = 0
        while temp > 0:
            digits += 1
            temp //= 10

    # compute sum of each digit^digits 
    temp = n
    total = 0
    while temp > 0:
        d = temp % 10
        # compute d**digits manually with a loop (avoids pow/**)
        p = 1
        for _ in range(digits):
            p *= d
        total += p
        temp //= 10

    # compare
    if total == n:
        print(f"{n} is an Armstrong number.")
    else:
        print(f"{n} is NOT an Armstrong number.")

