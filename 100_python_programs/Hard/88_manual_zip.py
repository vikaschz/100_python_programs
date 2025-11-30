"""
Program: Manual Zip
Description: Implement your own zip() function.

"""
def manual_zip(*lists):
    # Find smallest length among all given lists
    min_len = min(len(lst) for lst in lists)

    result = []
    for i in range(min_len):
        result.append(tuple(lst[i] for lst in lists))
    
    return result


# User inputs
A = list(map(int, input("Enter list A: ").split()))
B = list(map(int, input("Enter list B: ").split()))
C = list(map(int, input("Enter list C (optional, press Enter to skip): ").split() or []))

zipped = manual_zip(A, B, C)

print("\nManual Zip Result:", zipped)
