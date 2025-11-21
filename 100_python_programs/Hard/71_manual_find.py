"""
Program: Manual Find
Description: Implement your own find() for substring.

Hint:
- Scan using nested loops.

"""


def manual_find(text, pattern):
    n = len(text)
    m = len(pattern)

    # Edge case: empty pattern
    if m == 0:
        return 0

    # Try all starting positions
    for i in range(n - m + 1):
        match = True

        # Compare substring manually
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break

        if match:
            return i

    return -1


# Example usage
text = input("Enter main string: ")
pattern = input("Enter substring to find: ")

result = manual_find(text, pattern)

if result == -1:
    print("Substring not found")
else:
    print("Substring found at index:", result)
