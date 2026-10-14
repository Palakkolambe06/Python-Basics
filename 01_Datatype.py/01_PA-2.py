# Q2. Read all lines from a file into a list. Print the total number of lines and display the 2nd and 4th line.


# Open the file in read mode
with open("sample.txt", "r") as file:
    # Read all lines from the file and store them in a list
    lines = file.readlines()
# Calculate the total number of lines in the file
total_lines = len(lines)
# Display the total number of lines
print("Total number of lines:", total_lines)
# Check whether the file contains at least two lines
if total_lines >= 2:
    # Print the second line using index 1
    print("Second line:", lines[1].strip())
else:
    # Display a message if the second line is unavailable
    print("Second line does not exist")
# Check whether the file contains at least four lines
if total_lines >= 4:
    # Print the fourth line using index 3
    print("Fourth line:", lines[3].strip())
else:
    # Display a message if the fourth line is unavailable
    print("Fourth line does not exist")
