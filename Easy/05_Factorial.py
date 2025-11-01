"""
Program: Factorial of a Number
Difficulty: Easy
Description: Takes input from the user and prints n!. Handles invalid and negative inputs.

Example:
Input: 5
Output: 120
==> 5 * 4 * 3 * 2 * 1 = 120
"""

n = int(input("Enter n value: "))
        
if n < 0:
    print("Factorial is not defined for negative numbers ")
    
else:    
    fact = 1
    for i in range(1, n + 1):
        fact *= i #fact = fact*i

    print(f"Factorial of {n} is: {fact}")
