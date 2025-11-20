"""
Program: Area of circle
Description: Calculate the area of a circle given its radius using the formula A = πr²

Example:
Input: radius = 5
Output: Area = 78.54 square units
"""

radius = float(input("Enter radius of circle: "))
area = 3.142 * pow(radius, 2)
print(f"The area of circle: {area} square units")