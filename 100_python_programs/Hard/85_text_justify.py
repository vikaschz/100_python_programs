"""
Program: Text Justify
Description: Implement text justification with width.

"""
words = input("Enter words: ").split()
maxWidth = int(input("Enter line width: "))

lines = []         # stores final justified lines
current = []       # words in current line
curr_len = 0       # total characters of words in current line

# STEP 1: Group words line by line
for w in words:
    # if adding this word + spaces exceeds width, finalize line
    if curr_len + len(current) + len(w) > maxWidth:
        lines.append(current)
        current = []
        curr_len = 0

    current.append(w)
    curr_len += len(w)

# add last line
if current:
    lines.append(current)

result = []

# STEP 2: Justify each line manually
for i in range(len(lines)):
    line_words = lines[i]

    # LAST line → left justify
    if i == len(lines) - 1:
        line = " ".join(line_words)
        line += " " * (maxWidth - len(line))
        result.append(line)
        continue

    # Normal line justification
    if len(line_words) == 1:
        # Only one word → pad to right
        one = line_words[0] + " " * (maxWidth - len(line_words[0]))
        result.append(one)
        continue

    # Multiple words → distribute spaces manually
    total_char_len = sum(len(w) for w in line_words)
    total_spaces = maxWidth - total_char_len
    gaps = len(line_words) - 1

    space_each = total_spaces // gaps
    extra = total_spaces % gaps

    line = ""
    for j in range(gaps):
        line += line_words[j]
        line += " " * space_each
        if j < extra:
            line += " "
    line += line_words[-1]

    result.append(line)

# STEP 3: Print output
print("\nJustified Output:\n")
for r in result:
    print(repr(r))
