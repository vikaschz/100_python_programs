"""
Program: Simple Interest
Description: Given P, R, T, compute simple interest = (P × R × T) / 100
"""

p = float(input("Enter Principal Amount (P): "))
r = float(input("Enter Rate of Interest (R): "))
t = float(input("Enter Time in Years (T): "))

interest = (p * r * t) / 100

print("Simple Interest =",interest)
