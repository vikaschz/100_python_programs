"""
Program: Sum Prime Digits
Description: Sum prime digits in number.

"""
sum_of_prime_digits = 0
n = int(input("Enter the limit: "))

print("Prime numbers are:")

for num in range(2, n + 1):
    is_prime = True
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(num, end=" ")
        sum_of_prime_digits += num
print(f"\nThe sum of prime digits is: {sum_of_prime_digits}")





