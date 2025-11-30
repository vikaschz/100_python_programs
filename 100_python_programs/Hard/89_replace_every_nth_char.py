"""
Program: Replace Every Nth Char
Description: Replace every nth character in a string.

Hint:
- Use loop index.

"""
s = input("Enter a string: ")
n = int(input("Enter n value: "))
res = ""
for i, ch in enumerate(s):     
    if (i + 1) % n == 0:       
        res += "#"
    else:
        res += ch

print(res)
