"""
Program: Longest Unique Substring
Description: Find longest substring without repeating characters (no set).

Hint:
- Use sliding window manually.

"""
s = input("Enter a string: ")

start = 0
max_length = 0
last_seen = {}

for i in range(len(s)):
    ch = s[i]

    # If char was seen before AND inside current window
    if ch in last_seen and last_seen[ch] >= start:
        start = last_seen[ch] + 1

    # Update last seen index
    last_seen[ch] = i

    # Length of current window
    window_length = i - start + 1

    # Update max length
    max_length = max(max_length, window_length)

print("Longest unique substring length:", max_length)




