# Q7. Line Numbering

with open("sample.txt", "r") as file:
    lines = file.readlines()

n = 1

for line in lines:
    print(n, ":", line, end="")
    n = n + 1
