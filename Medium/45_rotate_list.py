"""
Program: Rotate List
Description: Rotate list right by k positions.

Hint:
- Use slicing or modular indexing.

"""
k = int(input("Enter k (number of rotations): "))
lst = [2, 4, 6, 8, 10]
k = k % len(lst)


rotated_list = lst[-k:] + lst[:-k]
print(rotated_list)


