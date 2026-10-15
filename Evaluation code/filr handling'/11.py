# Q11. Copy Even-Numbered Lines

with open("sample.txt", "r") as source:
    lines = source.readlines()

with open("even_lines.txt", "w") as destination:
    for number, line in enumerate(lines, start=1):
        if number % 2 == 0:
            destination.write(line)

print("Even Numbered Lines Copied Successfully")
