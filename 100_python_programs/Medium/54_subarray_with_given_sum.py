"""
Program: Subarray With Given Sum
Description: Find a contiguous subarray with sum S using sliding window (works for positive numbers).
"""

array = []
size = int(input("Enter size of array: "))
for i in range(1, size + 1):
    item = int(input(f"Enter item {i}: "))
    array.append(item)

target = int(input("Enter the sum value: "))

start = 0
current_sum = 0
found = False

for end, val in enumerate(array):
    current_sum += val
    while current_sum > target and start <= end:
        current_sum -= array[start]
        start += 1
    if current_sum == target:
        print(f"Subarray found from index {start} to {end}: {array[start:end+1]}")
        print(f"(1-based indices: {start+1} to {end+1})")
        found = True
        break

if not found:
    print("No subarray with given sum found")
