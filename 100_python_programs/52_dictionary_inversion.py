"""
Program: Dictionary Inversion
Description: Invert dictionary mapping values to list of keys.

"""

dict_inv = {}

my_dict = {
    "a": "red",
    "b": "blue",
    "c": "red",
    "d": "red",
    "e": "violet",
    "g": "blue",
    "h": "violet",
}

for key, value in my_dict.items():
    if value not in dict_inv:
        dict_inv[value] = []
    dict_inv[value].append(key)
        
print(dict_inv)

