"""
Program: Count Frequency
Description: Count frequency of elements.

Hint:
- Use dictionary to store counts.

"""
freq  = {} 
l = [7,8,9,4,4,5,5,4,2,2,5,5,0,5,5,8,5,6,2,5]
for element in l:
    if element in freq:
        freq[element] += 1
        
    else:
        freq[element] = 1

print(freq)