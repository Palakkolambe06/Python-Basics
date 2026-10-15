# Q10. File Comparison

with open("sample1.txt", "r") as file:
    content1 = file.read()

with open("sample2.txt", "r") as file:
    content2 = file.read()

if content1 == content2:
    print("Both files are same")
else:
    print("Both files are different")
