"""
Program: Check prime small
Description: Check if n is prime.

Example:
Input/Output:
17 -> Prime
"""

try:
    num = int(input("Enter a number: "))

    if num < 2:
        print(f"{num} is not Prime")
    elif num == 2:
        print(f"{num} is Prime")
    elif num % 2 == 0:
        print(f"{num} is not Prime")
    else:
        is_prime = True
        i = 3
        while i * i <= num:
            if num % i == 0:
                is_prime = False
                break
            i += 2
        
        if is_prime:
            print(f"{num} is Prime")
        else:
            print(f"{num} is not Prime")

except ValueError:
    print("Please enter a valid integer")





