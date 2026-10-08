# Create dictionary with studnet details
student = {
    101:{"Name": "Aditi", "Scores":[78, 85, 90]},
    102:{"Name": "Rahul", "Scores":[45, 60, 50]},
    103:{"Name": "Sneha", "Scores":[90, 80, 95]},
    104:{"Name": "Nishi", "Scores":[66, 77, 88]},
    105:{"Name": "Ashvitha", "Scores":[50, 55, 20]},
}

# Calculate the average score and flag pass/fail
for sid, details in student.items():
    avg = sum(details["Scores"]) / len(details["Scores"])
    details["Average"] = avg
    details["Passed"] = avg >= 50 # Boolean flag

# Print names of students who passed 
print("Students who passed: ")
for sid, details in student.items():
    if details["Passed"]:
        print(details["Name"])

# Print names of students who fail
for sid, details in student.items():
    avg = sum(details["Scores"]) / len(details["Scores"])
    details["Average"] = avg
    details["Passed"] = avg >= 50
    print(details["Average"])

# Write a program to guess a number
# Write a program to guess a number

number = int(input("Enter your guessed number: "))

if number <= 0:
    print("The number is invalid. Your guess is wrong")

elif number == 1:
    print('Congratulations!!! - Your guessed number "1" is correct.')

elif number == 2:
    print('Congratulations!!! - Your guessed number "2" is correct.')

elif number == 3:
    print('Congratulations!!! - Your guessed number "3" is correct.')

elif number == 4:
    print('Congratulations!!! - Your guessed number "4" is correct.')

elif number == 5:
    print('Congratulations!!! - Your guessed number "5" is correct.')

elif number == 6:
    print('Congratulations!!! - Your guessed number "6" is correct.')

elif number == 7:
    print('Congratulations!!! - Your guessed number "7" is correct.')

elif number == 8:
    print('Congratulations!!! - Your guessed number "8" is correct.')

elif number == 9:
    print('Congratulations!!! - Your guessed number "9" is correct.')

elif number == 10:
    print('Congratulations!!! - Your guessed number "10" is correct.')

else:
    print("You are a fool!!!")

# Create a dictionary for library
# Craete a list of numbers and strings and set the values from user. & seperate the lsit from the maximum number. Display the names in a sorted order or descending order.
# Make names from you name .

library = {
    1 : {"Book Name" : "Ikigai" , "Author Name" :"Héctor García" , "Available" : "Yes", "Price" : 400} , 
    2 : {"Book Name" : "Atomic Habits " , "Author Name" :"James Clear" , "Available" : "Yes", "Price" : 300} , 
    3 : {"Book Name" : "Phsycology of Money " , "Author Name" :"Morgan Housel " , "Available" : "No", "Price" : 600} , 
}
print(library)

# Make names from you name .
name = "Palak Kolambe"
print("Possible meaningful names:")
print("Kamal")
print("Alka")
print("Alok")
print("Kopal")
print("Komal")

# Find vowels from your name using a loop

name = "Palak Kolambe"
vowels = "aeiouAEIOU"
for letter in name:
    if letter in vowels:
        print(letter)
    