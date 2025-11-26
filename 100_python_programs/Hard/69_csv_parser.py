"""
Program: Csv Parser
Description: Parse CSV including quoted values.

"""
def parse_csv(text):
    rows = []
    row = []
    field = ""
    inside_quotes = False
    i = 0
    n = len(text)

    while i < n:
        ch = text[i]

        # --------------------------
        # Case 1: Inside quotes
        # --------------------------
        if inside_quotes:
            if ch == '"':
                # Check for escaped quote ""
                if i + 1 < n and text[i + 1] == '"':
                    field += '"'
                    i += 1  # Skip the second quote
                else:
                    inside_quotes = False  # Quote closed
            else:
                field += ch

        # --------------------------
        # Case 2: Outside quotes
        # --------------------------
        else:
            if ch == '"':
                inside_quotes = True

            elif ch == ',':
                row.append(field)
                field = ""

            elif ch == '\n':
                row.append(field)
                rows.append(row)
                row = []
                field = ""

            else:
                field += ch

        i += 1

    # Add last field and row
    row.append(field)
    rows.append(row)

    return rows


# Example usage
csv_text = '''"Name","Age","City"
"Vikas",20,"New Delhi"
"John ""The King"" Doe",35,"Los Angeles"'''

result = parse_csv(csv_text)

for r in result:
    print(r)
