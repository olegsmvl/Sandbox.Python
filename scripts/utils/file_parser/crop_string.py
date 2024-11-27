import os

filtered = ""
word = "test::"

with open("test_file.txt", "r") as file:
    for line in file:
        start = line.find(word)
        if start != -1:
            crop_begin = line[start:]
            end = crop_begin.find(" ")
            filtered += crop_begin[:end] + "\n"

print(filtered)
