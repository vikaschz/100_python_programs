"""
Program: Unique elements
Description: Return list of unique elements preserving order.

Example:
Input/Output:
[1,2,2,3] -> [1,2,3]
"""

l = [1,2,1,3,3,3,3,33,3,2,3]
unique_element = []

for num in l:
    if num not in unique_element:
        unique_element.append(num)
print(unique_element)

