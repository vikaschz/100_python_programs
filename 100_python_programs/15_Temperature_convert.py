"""
Program: Temperature Converter
Description: Convert temperatures from Celsius to Fahrenheit using the formula:
            °F = (°C × 9/5) + 32
            

Example:
qtInput: 100°C
Output: 212°F

"""
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit:.1f}°F")

