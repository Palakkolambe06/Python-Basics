# Display numbers from -10 to -1
for i in range(-10, 0):
    print(i)

# Calculate the sum of numbers from 1 to n in a given list 
list = [1, 2, 3, 4, 5]
sum = 0
for i in list:
    sum = sum + i
print("The sum of the given list is:", sum)

# Write a program to calculate the average of a given list of numbers
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num    
average = total / len(numbers)  
print("The average of the given list is:", average) 