import os


i = 0

filtered = ""
word = "test"

with open("test_file.txt", "r") as file:
    for line in file:
        i += 1
        # print(line.strip())
        if word in line:
            filtered += line

print(filtered)
