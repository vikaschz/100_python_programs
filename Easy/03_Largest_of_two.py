"""
Program: Largest of two numbers
Difficulty: Easy
Description: Take input from user and print the larger one.

Example:
Input: 5 2 
Output: 5 is the largest number
"""


def main():
    num_1 = int(input("Enter number: "))
    num_2 = int(input("Enter number: "))
    print(
        f"{num_1} is the largest number"
        if num_1 > num_2
        else f"{num_2} is the largest number"
    )


if __name__ == "__main__":
    main()
