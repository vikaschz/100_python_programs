"""
Program: String Rotation Check
Description: Check if two strings are rotations of each other.
"""

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if len(str1) == len(str2) and str2 in (str1 + str1):
    print("Strings are rotations of each other.")
else:
    print("Strings are NOT rotations of each other.")
