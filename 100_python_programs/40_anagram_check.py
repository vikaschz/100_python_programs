"""
Program: Anagram Check
Description: Check if two strings are anagrams.

"""

word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

if sorted(word1) == sorted(word2):
    print("Anagram")
else:
    print("Not an Anagram")



