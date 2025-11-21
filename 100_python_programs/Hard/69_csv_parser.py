"""
Program: Csv Parser
Description: Parse CSV including quoted values.

"""
def parse_csv(text):
    rows = []
    row = []
    field = ""
    i = 0
    inside_quotes = False
    n = len(text)

    while i < n:
        char = text[i]

        # --- Inside quoted field ---
        if inside_quotes:
            if char == '"':
                # Check for escaped quote ("")
                if i + 1 < n and text[i + 1] == '"':
                    field += '"'
                    i += 1  # Skip next quote
                else:
                    inside_quotes = False  # Closing quote
            else:
                field += char

        # --- Outside quoted field ---
        else:
            if char == '"':
                inside_quotes = True

            elif char == ',':
                row.append(field)
                field = ""

            elif char == '\n':
                row.append(field)
                rows.append(row)
                row = []
                field = ""

            else:
                field += char

        i += 1

    # Add last field/row if file doesn't end with newline
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
