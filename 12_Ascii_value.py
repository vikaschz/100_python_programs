"""
Program: ASCII value
Description: Print ASCII value of given character.
"""

char = input("Enter a character: ")
if len(char) == 1:
    # Get ASCII value using ord() function
    ascii_value = ord(char)
    print(f"ASCII value of '{char}' is {ascii_value}")
else:
    print("Please enter a single character")
