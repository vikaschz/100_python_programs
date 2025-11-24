"""
Program: Unique Pangram Check
Description: Check pangram ignoring duplicates.

Hint:
- Track each letter only once.

"""

alphabets = {
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
}
found = set()
sentence = input("Enter the sentence: ").lower()

for ch in sentence:
    if ch in alphabets:
        found.add(ch)
if found == alphabets:
    print("The sentence is pangram")
else:
    print("The sentence is not pangram")

