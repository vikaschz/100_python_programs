"""
Program: String Compression
Description: Compress repeated characters like aaabb → a3b2.


"""
string = input("Enter a string: ")

result = ""
count = 1

for i in range(len(string)):
    if i < len(string) - 1 and string[i] == string[i+1]:
        count += 1
    else:
        result += string[i] + str(count)
        count = 1

print(result)


