"""
Program: Sum Of Two Lists Elementwise
Description: Add elements of two lists.

"""

list_1 = [1, 2, 3, 4, 5, 2, 6]
list_2 = [2, 4, 6, 8, 10, 1, 1, 1, 23, 45, 6]

sum_of_two_list = []

while len(list_1) != len(list_2):
    if len(list_1) > len(list_2):
        list_2.append(0)
    else:
        list_1.append(0)

for i in range(len(list_1)):
    sum = list_1[i] + list_2[i]
    sum_of_two_list.append(sum)


print(f"sum of two list is: {sum_of_two_list}")
