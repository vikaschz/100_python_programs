"""
Program: Swap Two Numbers
Difficulty: Easy
Description: Given two numbers A and B, output them swapped.

Example:
Input: A=3 B=8
Output: A=8 B=3
"""

def main():
    a = int(input("Enter A: "))
    b = int(input("Enter B: "))
    print(f"Before swapping\nA = {a}\nB = {b}")
    a,b = b,a
    print(f"After swapping\nA = {a}\nB = {b}")
    

if __name__ == "__main__":
    main()
