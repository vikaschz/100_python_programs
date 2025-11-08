"""
Program: Binary Search
Description: Return index of key in sorted list.
"""

lst = [3,4,1,2,6,7,8,5,9]
lst.sort()      
print("Sorted List:", lst)

key = int(input("Enter key value: "))

low = 0
high = len(lst) - 1

found = False

while low <= high:
    mid = (low + high) // 2
    
    if lst[mid] == key:
        print(f"Index of value {key} is: {mid}")
        found = True
        break
    
    elif key < lst[mid]:
        high = mid - 1
    else:
        low = mid + 1

if not found:
    print(f"{key} not found in the list.")
