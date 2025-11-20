"""
Program: Count Inversions
Description: Count inversions where a[i] > a[j].
"""

lst = []
size = int(input("Enter the size of list: "))
for _ in range(1, size+1):
    item = int(input(f"Enter item {_}: "))
    lst.append(item)

count = 0
for i in range(len(lst)-1):
    for j in range(i+1 , len(lst)):
        if lst[i] > lst[j]:
            count = count + 1
print(f"Total inversions is: {count}")

