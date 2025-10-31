"""
Program: Simple Interest
Difficulty: Easy
Description: Given P, R, T, compute simple interest = (P × R × T) / 100
"""

def simple_interest():
    p = float(input("Enter Principal Amount (P): "))
    r = float(input("Enter Rate of Interest (R): "))
    t = float(input("Enter Time in Years (T): "))

    interest = (p * r * t) / 100
    return interest

print("Simple Interest =", simple_interest())
