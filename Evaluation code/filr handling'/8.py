# Q8. Reverse File Content (Word Order)

with open("sample.txt", "r") as file:
    lines = file.readlines()

with open("reverse.txt", "w") as file:
    for line in lines:
        words = line.split()
        words.reverse()
        file.write(" ".join(words) + "\n")

with open("reverse.txt", "r") as file:
    print(file.read())

print("Words reversed successfully.")
