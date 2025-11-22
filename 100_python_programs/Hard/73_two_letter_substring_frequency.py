"""
Program: Two Letter Substring Frequency
Description: Count all 2-letter substring frequencies.

Hint:
- Loop and take s[i:i+2].

"""


text = input("Enter a string: ")

freq = {}
for i in range(len(text) - 1):
    pair = text[i:i+2]   # 2-letter substring
    if pair in freq:
        freq[pair] += 1
    else:
        freq[pair] = 1

print("2-letter substring frequencies:")
for k, v in freq.items():
    print(k, ":", v)


