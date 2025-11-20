"""
Program: Remove Duplicates Sorted
Description: Remove duplicates from sorted list.

Hint:
- Iterate and compare previous element.

"""
unique_list = []
l = [7,8,9,4,4,5,5,4,2,2,5,5,0,1,3,5,5,8,5,6,2,5]
sort = sorted(l)

for n in sort:
    if n not in unique_list:
        unique_list.append(n)
print(unique_list)






