"""
Program: Reverse the number
Difficulty: Easy
Description: print the reverse of a number
"""

def reverse_number(num):
    temp = num
    rev = ""

    while temp>0:
        digit  = temp%10
        rev +=str(digit)
        temp//=10

    return f"Reversed: {rev}"
    

number = int(input('Enter a number: '))
print(reverse_number(number))
