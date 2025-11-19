"""
Program: Longest Word In Sentence
Description: Find longest word in sentence.

Hint:
- Use split() and comparisons.

"""
s = input("Enter a sentence: ").split()

longest = ''

for word in s:
    if len(word) > len(longest):
        longest = word

print(f"Longest word: '{longest}'")



