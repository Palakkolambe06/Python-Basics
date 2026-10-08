# STRING FUNCTIONS 

# 1. strip()
# Removes spaces from both the beginning and end of a string
text = "   Hello Python   "
print("strip():", text.strip())


# 2. lstrip()
# Removes spaces from the left side of a string
text = "   Hello Python"
print("lstrip():", text.lstrip())


# 3. rstrip()
# Removes spaces from the right side of a string
text = "Hello Python   "
print("rstrip():", text.rstrip())


# 4. replace()
# Replaces one part of a string with another
text = "I love Python"
print("replace():", text.replace("Python", "Java"))


# 5. split()
# Splits a string into a list
text = "Python is easy"
print("split():", text.split())


# LIST FUNCTIONS 

# 6. clear()
# Removes all elements from a list
numbers = [10, 20, 30, 40]
numbers.clear()
print("clear():", numbers)


# 7. index()
# Returns the position (index) of an element
numbers = [10, 20, 30, 40]
print("index():", numbers.index(30))


# 8. count()
# Counts how many times an element appears in a list
numbers = [10, 20, 20, 30, 20]
print("count():", numbers.count(20))


# 9. sort()
# Arranges the elements of a list in ascending order
numbers = [40, 10, 30, 20]
numbers.sort()
print("sort():", numbers)


# 10. reverse()
# Reverses the order of elements in a list
numbers = [10, 20, 30, 40]
numbers.reverse()
print("reverse():", numbers)

'''strip(): Hello Python
lstrip(): Hello Python
rstrip(): Hello Python
replace(): I love Java
split(): ['Python', 'is', 'easy']
clear(): []
index(): 2
count(): 3
sort(): [10, 20, 30, 40]
reverse(): [40, 30, 20, 10]'''