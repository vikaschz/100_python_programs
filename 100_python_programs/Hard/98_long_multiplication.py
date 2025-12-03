"""
Program: long multiplication
Description: Multiply huge numbers manually. 
"""

def long_multiply(num1, num2):
    n1 = num1[::-1]
    n2 = num2[::-1]

    # Result can be at most len1 + len2 digits
    result = [0] * (len(num1) + len(num2))

    # Multiply each digit
    for i in range(len(n1)):
        for j in range(len(n2)):
            result[i + j] += int(n1[i]) * int(n2[j])

            # Handle carry
            result[i + j + 1] += result[i + j] // 10
            result[i + j] %= 10

    # Remove leading zeros from the back
    while len(result) > 1 and result[-1] == 0:
        result.pop()

    # Convert digits back to a string
    return ''.join(map(str, result[::-1]))


a = input("Enter first big number: ")
b = input("Enter second big number: ")

print("Product =", long_multiply(a, b))
