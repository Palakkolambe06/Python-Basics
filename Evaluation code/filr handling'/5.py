# Q5. Append Text to a File

with open("sample.txt", "a") as file:
    file.write("\nThis is Appended Txt Palak Kolambe")

with open("sample.txt", "r") as file:
    print(file.read())
