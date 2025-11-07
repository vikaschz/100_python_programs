"""
Program: Median Of Two Sorted Lists
Description: Find median by merging two sorted lists.

"""

l1 = [9,6,4,2,7]
l2 = [3,10,1,5,8]

merged = sorted(l1) + sorted(l2)
sort = sorted(merged)
print("Sorted List:", sort)


n = len(sort)

if n % 2 != 0:      
    median = sort[n // 2]
else:               
    median = (sort[n//2 - 1] + sort[n//2]) / 2

print("Median:", median)
