"""
Program: ATM Simulation
Description: Simulate ATM withdrawal logic.
"""

notes = {
    "₹2000": 10,
    "₹500": 10,
    "₹200": 15,
    "₹100": 30,
    "₹50": 20,
    "change": 10000     # not used for withdrawal
}

# ---- Calculate total balance ----
balance = 0
for note, count in notes.items():
    if note.startswith("₹"):       # skip "change"
        value = int(note.replace("₹", ""))
        balance += value * count

print("Current balance in ATM:", balance)

# ---- Input withdrawal amount ----
withdraw = int(input("Enter withdrawal amount: "))

# ---- Basic validations ----
if withdraw > balance:
    print("Not enough money in ATM.")
    exit()

if withdraw % 50 != 0:
    print("Amount must be multiples of ₹50.")
    exit()

# ---- Withdrawal logic ----
to_give = {}  # store notes to dispense
amount_left = withdraw

# Sort notes from highest to lowest
sorted_notes = sorted(
    [n for n in notes.keys() if n.startswith("₹")],
    key=lambda x: int(x.replace("₹", "")),
    reverse=True
)

for note in sorted_notes:
    note_value = int(note.replace("₹", ""))
    available = notes[note]

    if amount_left >= note_value and available > 0:
        needed = amount_left // note_value
        giving = min(needed, available)

        if giving > 0:
            to_give[note] = giving
            amount_left -= giving * note_value

# ---- Check if withdrawal possible ----
if amount_left != 0:
    print("Cannot dispense the exact amount with available notes.")
    exit()

# ---- Update ATM note counts ----
for note, cnt in to_give.items():
    notes[note] -= cnt

# ---- Output ----
print("\nWithdrawal successful!")
print("Dispensed notes:")

for n, c in to_give.items():
    print(f"{n} x {c}")

print("\nRemaining notes in ATM:")
for n, c in notes.items():
    print(n, "=", c)
