# Q3. Take a sentence from the user, split it into words, and store them in a list. Print the longest word.


# Accept a sentence from the user
sentence = input("Enter a sentence: ")
# Split the sentence into individual words
words = sentence.split()
# Check whether the list contains any words
if words:
    # Find the longest word using the length of each word
    longest_word = max(words, key=len)
    # Display the list of words
    print("List of words:", words)
    # Display the longest word
    print("Longest word:", longest_word)
    # Display the length of the longest word
    print("Length of longest word:", len(longest_word))
else:
    # Handle the case where the user enters an empty sentence
    print("No words found in the sentence")
