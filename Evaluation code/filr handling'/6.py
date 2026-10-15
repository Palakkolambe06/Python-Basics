# Q6. Seek Practice

with open("sample.txt", "r") as file:
    file.seek(10)
    print(file.read(5))
