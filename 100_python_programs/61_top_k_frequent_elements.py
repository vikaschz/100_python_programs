"""
Program: Top K Frequent Elements
Description: Find the K most frequent elements.
"""

# Step 1: Input elements
freq = {}
n = int(input("Enter number of elements: "))

elements = []
for i in range(n):
    elem = int(input(f"Enter element {i+1}: "))
    elements.append(elem)

# Step 2: Count frequency
for num in elements:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

# Step 3: Input K
k = int(input("Enter K (top frequent elements): "))

# Step 4: Sort items by frequency (descending)
sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

# Step 5: Take top-K
top_k = sorted_items[:k]

# Step 6: Print result
print(f"Top {k} frequent elements are:")
for num, count in top_k:
    print(num)

