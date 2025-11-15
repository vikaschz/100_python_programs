"""
Program: Merge Intervals
Description: Merge overlapping intervals.

"""

result = []
lst = [[1, 3], [2, 6], [8, 10], [15, 18]]
sorted_list = sorted(lst)

result.append(sorted_list[0])

for l in sorted_list:
    current = l
    last = result[-1]

    last_start = last[0]
    last_end = last[1]
    current_start = current[0]
    current_end = current[1]
    if current_start <= last_end:
        merged_end = max(last_end, current_end)
        a = [last_start, merged_end]
        result.pop()
        result.append(a)
    else:
        result.append(l)

print(result)
