# 1. create a lsit of 10 number. 
# 2. Print the sum of last 4 elemnets of the lsit.
# 3. Find out the difference betweeb maximum and minimum elemnet of the list.
# 4. Insert a number in a list at 6th position - this number must be 1/3 of number stored at 4th position. 

# 1. Create a list of 10 numbers
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Original list:", numbers)

# 2. Print the sum of the last 4 elements of the list
# Last 4 elements are:
# 70, 80, 90, 100
last_four_sum = sum(numbers[-4:])
print("Sum of last 4 elements:", last_four_sum)

# 3. Find the difference between maximum and minimum element of the list
maximum = max(numbers)
minimum = min(numbers)
difference = maximum - minimum

print("Maximum element:", maximum)
print("Minimum element:", minimum)
print("Difference:", difference)

# 4. Insert a number at 6th position, The number must be 1/3 of the number stored at 4th position.
# Python indexing starts from 0.
# 4th position = index 3
# 6th position = index 5
number_to_insert = numbers[3] / 3

# Insert the calculated number at index 5
numbers.insert(5, number_to_insert)

print("List after inserting the number:", numbers)

name = "palakkolmabe" 
maximum = max(name)
minimum = min(name)
difference = maximum - minimum

print("Maximum element:", maximum)
print("Minimum element:", minimum)
print("Difference:", difference)