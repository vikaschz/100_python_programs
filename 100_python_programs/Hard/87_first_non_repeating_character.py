"""
Program: First Non-Repeating Character
Description: Find the first character in a string that does not repeat.
"""

s = input("Enter a string: ").lower()

# Step 1: Count frequencies
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

# Step 2: Find first character with frequency 1
for ch in s:
    if freq[ch] == 1:
        if ch == " ":
            print("The first non repeating character is: space")
        else:
            print(f"The first non repeating character is: {ch}")
        break
else:
    print("No non-repeating character found.")
