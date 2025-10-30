"""
Program: Factorial of a Number
Difficulty: Easy
Description: Takes input from the user and prints n!. Handles invalid and negative inputs.

Example:
Input: 5
Output: 120
"""

def main():
    try:
        n = int(input("Enter n value: "))
        
        if n < 0:
            print("Factorial is not defined for negative numbers ")
            return
        
        fact = 1
        for i in range(1, n + 1):
            fact *= i

        print(f"Factorial of {n} is: {fact}")

    except ValueError:
        print("Invalid input! Please enter an integer number.")


if __name__ == "__main__":
    main()
