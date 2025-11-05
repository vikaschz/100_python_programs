"""
Program: Count Primes In Range
Description: Count primes in range [a,b].
"""

a = int(input("Enter starting number: "))
b = int(input("Enter ending number: "))

count = 0

for num in range(a, b+1):
    if num > 1:  
        is_prime = True
        for i in range(2, num):
            if num % i == 0:   
                is_prime = False
                break
        if is_prime:
            count += 1

print("Total prime numbers:", count)
