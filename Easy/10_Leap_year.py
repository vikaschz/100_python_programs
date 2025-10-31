"""
Program: Leap year
Difficulty: Easy
Description: Check if a year is leap (Gregorian).
"""

def is_leap_year(year):
    # Leap year conditions:
    # 1. Divisible by 4
    # 2. Not divisible by 100 unless also divisible by 400
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

year = int(input("Enter the year: "))
if is_leap_year(year):
    print("Leap Year")
else:
    print("Not a Leap Year ")
