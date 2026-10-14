# Q4. Read a file, split its content into words, and store them in a list. (i) Print the total number of words. (ii) Print all unique words.


# Open the file in read mode
with open("sample.txt", "r") as file:
    # Read the complete content of the file
    content = file.read()
# Split the content into individual words
words = content.split()
# Count the total number of words in the list
total_words = len(words)
# Display the total number of words
print("Total number of words:", total_words)
# Convert each word to lowercase to avoid case-sensitive duplicates
lowercase_words = [word.lower() for word in words]
# Use a set to identify unique words
unique_words = set(lowercase_words)
# Display all unique words
print("Unique words:", unique_words)
# Display the number of unique words
print("Number of unique words:", len(unique_words))
