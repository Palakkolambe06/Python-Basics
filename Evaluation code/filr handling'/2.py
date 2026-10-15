# Q2. Write and Read Back

with open("sample.txt", "w") as file:
    file.write("Welcome to the Magical World of Python")

with open("sample.txt", "r") as file:
    print(file.read())
