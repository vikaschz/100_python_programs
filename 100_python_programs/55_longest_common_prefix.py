"""
Program: Longest Common Prefix
Description: Find longest common prefix among strings.

Example:
Input: ["flower", "flow", "flight"]
Output: "fl"
"""



# Input number of words
n = int(input("Enter number of words: "))

words = []

# Input the words
for i in range(n):
    w = input(f"Enter word {i+1}: ")
    words.append(w)

# Take the first word as prefix
prefix = words[0]

# Compare prefix with each next word
for word in words[1:]:

    # While prefix is not at the start of the word, shrink prefix
    while not word.startswith(prefix):
        prefix = prefix[:-1]   # remove last character

        # If prefix gets empty, no common prefix
        if prefix == "":
            break


print(f"Longest Common Prefix = '{prefix}'")
