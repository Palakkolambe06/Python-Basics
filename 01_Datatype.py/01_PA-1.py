# Q1. Write a program to read a file and count how many vowels are present in its content.

# Open the file in read mode
with open("sample.txt", "r") as file:
    # Read the complete content of the file
    content = file.read()
# Initialize the vowel counter
vowel_count = 0
# Define all vowels in lowercase
vowels = "aeiou"
# Convert the content to lowercase and check each character
for character in content.lower():
    # Check whether the character is a vowel
    if character in vowels:
        # Increase the counter by one
        vowel_count += 1
# Display the total number of vowels
print("Total number of vowels:", vowel_count)
