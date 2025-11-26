"""
Program: Merge Time Ranges
Description: Merge overlapping time ranges.

Hint:
- Convert to minutes and compare.

"""
# Input time ranges
time_ranges = []
n = int(input("Enter number of ranges: "))

for i in range(1, n + 1):
    t = tuple(map(int, input(f"Range {i} (start end): ").split()))
    time_ranges.append(t)

# Step 1: Sort ranges by start time
time_ranges.sort()

# Step 2: Merge logic
merged = []
merged.append(time_ranges[0])

for current in time_ranges[1:]:
    last_start, last_end = merged[-1]
    curr_start, curr_end = current

    # If overlapping: merge
    if curr_start <= last_end:
        merged[-1] = (last_start, max(last_end, curr_end))
    else:
        merged.append(current)

# Final output
print("Merged ranges:")
for r in merged:
    print(r[0], r[1])







               



