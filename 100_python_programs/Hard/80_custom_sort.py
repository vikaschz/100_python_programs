"""
Program: Custom Sort
Description: Implement sorting without using sort().

Hint:
- Use your own logic.

"""
# Custom Sort Program: Implement sorting without using sort() or min()

num = list(map(int, input("Enter numbers: ").split()))
sorted_list = []

temp = num[:]     # copy original list

while temp:
    # find smallest manually
    smallest = temp[0]
    for n in temp:
        if n < smallest:
            smallest = n
    
    sorted_list.append(smallest)
    temp.remove(smallest)

print(sorted_list)
