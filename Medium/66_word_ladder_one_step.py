"""
Program: Word Ladder One Step
Description: Check if two words differ by one character.

"""

differ = 0
first_word = input("Enter first word: ")
second_word = input("Enter second word(same length as first word): ")

if len(first_word) != len(second_word):
    print("Invalid, both words should have same length.")
else:

    for i in range(len(first_word)):
        if first_word[i] != second_word[i]:
            differ += 1
    if differ == 1:
        print(f"'{first_word}' and '{second_word}' differ by one character (1 mismatch).")
        print("This is a valid 'Word Ladder One Step'.")
    elif differ == 0:
        print(f"'{first_word}' and '{second_word}' are the same (0 mismatches).")
    else:
        print(f"'{first_word}' and '{second_word}' differ by {differ} characters.")
        print("This is not a valid 'Word Ladder One Step'.")