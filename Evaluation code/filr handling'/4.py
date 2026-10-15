# Q4. Print the Third Line

with open("sample.txt", "r") as file:
    lines = file.readlines()

if len(lines) >= 3:
    print(lines[2])
else:
    print("The file has less than three lines.")
