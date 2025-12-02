"""
Program: pattern sentence match
Description: Sentence follows letter pattern.
"""

def pattern_match(pattern, sentence):
    words = sentence.split()

    # 1. Length must match
    if len(pattern) != len(words):
        return False

    char_to_word = {}
    word_to_char = {}

    # 2. Check mapping for each position
    for ch, word in zip(pattern, words):

        # If the pattern character already has a mapping
        if ch in char_to_word:
            if char_to_word[ch] != word:
                return False
        else:
            char_to_word[ch] = word

        # If the word already maps to another pattern character
        if word in word_to_char:
            if word_to_char[word] != ch:
                return False
        else:
            word_to_char[word] = ch

    return True


pattern = input("Enter pattern: ")
sentence = input("Enter sentence: ")

if pattern_match(pattern, sentence):
    print("Sentence follows the pattern")
else:
    print("Sentence does NOT follow the pattern")
