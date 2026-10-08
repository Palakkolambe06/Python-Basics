'''# 1. Print the sum of first 10 even numbers
even = (0, 2, 4, 6, 8, 10, 12, 14, 16, 18)
print(sum(even))

# Accept 2 values S and N and print square of first N numbers starting from S
S = int(input("Enter a number: ")) # s is the starting number 
N = int(input("Enter a number: ")) 
print(S**2, (S+1)**2, (S+2)**2, (S+3)**2, (S+4)**2, (S+5)**2, (S+6)**2, (S+7)**2, (S+8)**2, (S+9)**2, sep=", ")

# Reverese the accepted string and print it
S = input("Enter a string:")
print(S[::-1])

# Accept sentence from user and count teh vowels
sentence = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
count = 0
for char in sentence:
    if char in vowels:
        count += 1
print("Number of vowels:", count)

# Remove duplicates from thw list
numbers = [1, 2, 3, 2, 4, 5, 1, 6]
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
print("List after removing duplicates:", unique)

# Reverse the list 
numbers = [1, 2, 3, 4, 5]
reversed = numbers[::-1]
print("Reversed list:", reversed)
'''

'''print following pattern
*
**
***
****
'''
symbols = ["&", "*", "$", "@", "#"]
for row, symbol in enumerate(symbols, start=1):
    print(" " * (len(symbols) - row) + symbol * (2 * row - 1))
