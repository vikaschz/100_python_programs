"""
Program: word abbreviation generator
Description: Generate logic-based word abbreviations.
"""
def abbrev_no_vowels(word):
    vowels = "aeiouAEIOU"
    result = word[0]   

    for ch in word[1:]:
        if ch not in vowels:
            result += ch

    return result


w = input("Enter a word: ")
print("Abbreviation:", abbrev_no_vowels(w))
