# PYTHON STRING METHODS

# 1. capitalize()
# Converts the first character to uppercase
# and the remaining characters to lowercase.
text = "hello WORLD"
print(text.capitalize())
# Output: Hello world

# 2. casefold()
# Converts the string to lowercase.
# Mainly useful for case-insensitive comparisons.
text = "HELLO World"
print(text.casefold())
# Output: hello world

# 3. center()
# Centers the string within the given width.
# The second argument specifies the filling character.
text = "Python"
print(text.center(20))
# Output:       Python
print(text.center(20, "-"))
# Output: -------Python-------

# 4. count()
# Counts how many times a specified value occurs.
text = "banana"
print(text.count("a"))
# Output: 3

text = "Python is easy. Python is powerful."
print(text.count("Python"))
# Output: 2

# 5. encode()
# Converts the string into bytes using an encoding.
# UTF-8 is commonly used.
text = "Hello"
print(text.encode())
# Output: b'Hello'

print(text.encode("utf-8"))
# Output: b'Hello'

# 6. endswith()
# Returns True if the string ends with the specified value.
# Otherwise returns False.
text = "Hello Python"
print(text.endswith("Python"))
# Output: True

print(text.endswith("Hello"))
# Output: False

# 7. expandtabs()
# Replaces tab characters (\t) with spaces.
# The number specifies the tab size.
text = "Hello\tWorld"
print(text.expandtabs(10))
# Output: Hello     World

# 8. find()
# Searches for a value and returns its FIRST position.
# If the value is not found, it returns -1.
text = "Hello Python"
print(text.find("Python"))
# Output: 6

print(text.find("Java"))
# Output: -1

# 9. format()
# Inserts values into placeholders {} in a string.
name = "Palak"
age = 21

text = "My name is {} and I am {} years old."

print(text.format(name, age))
# Output: My name is Palak and I am 21 years old.

# Using numbered placeholders
print("Name: {0}, Age: {1}".format(name, age))
# Output: Name: Palak, Age: 21

# 10. format_map()
# Formats a string using values from a dictionary.
# ------------------------------------------------------------

student = {
    "name": "Palak",
    "age": 21
}

text = "My name is {name} and I am {age} years old."

print(text.format_map(student))
# Output: My name is Palak and I am 21 years old.

# 11. index()
# Searches for a value and returns its FIRST position.
# If the value is not found, it raises ValueError.
text = "Hello Python"

print(text.index("Python"))
# Output: 6
# Uncomment the next line to see the error:
# print(text.index("Java"))
# ValueError

# 12. isalnum()
# Returns True if all characters are letters or numbers.
# Spaces and special characters make it False.
print("Python123".isalnum())
# Output: True

print("Python 123".isalnum())
# Output: False

# 13. isalpha()
# Returns True if all characters are alphabets.
# Numbers, spaces and special characters return False.
print("Python".isalpha())
# Output: True

print("Python123".isalpha())
# Output: False

# 14. isascii()
# Returns True if all characters are ASCII characters.
print("Hello123".isascii())
# Output: True

print("Café".isascii())
# Output: False

# 15. isdecimal()
# Returns True if all characters are decimal characters.
print("12345".isdecimal())
# Output: True

print("123abc".isdecimal())
# Output: False

# 16. isdigit()
# Returns True if all characters are digits.
print("12345".isdigit())
# Output: True

print("123abc".isdigit())
# Output: False

# 17. isidentifier()
# Checks whether the string is a valid Python identifier.
# Example: variable names are identifiers.
print("student_name".isidentifier())
# Output: True

print("student1".isidentifier())
# Output: True

print("1student".isidentifier())
# Output: False

print("student name".isidentifier())
# Output: False

# 18. islower()
# Returns True if all cased characters are lowercase.
print("hello".islower())
# Output: True

print("Hello".islower())
# Output: False

# 19. isnumeric()
# Returns True if all characters are numeric.
print("12345".isnumeric())
# Output: True

print("123abc".isnumeric())
# Output: False

# 20. isprintable()
# Returns True if all characters are printable.
# Newline and tab characters are not printable.
print("Hello World".isprintable())
# Output: True

print("Hello\nWorld".isprintable())
# Output: False

# 21. isspace()
# Returns True if all characters are whitespace.
# Examples: spaces, tabs and newlines.
print("   ".isspace())
# Output: True

print("\t".isspace())
# Output: True

print("Hello".isspace())
# Output: False

# 22. istitle()
# Returns True if the string follows title-case rules.
print("Hello World".istitle())
# Output: True

print("hello world".istitle())
# Output: False

# 23. isupper()
# Returns True if all cased characters are uppercase.
print("HELLO".isupper())
# Output: True

print("Hello".isupper())
# Output: False

# 24. join()
# Joins elements of a list/iterable into one string.
# The string before join() is inserted between elements.
names = ["Palak", "Riya", "Ananya"]

print(", ".join(names))
# Output: Palak, Riya, Ananya

words = ["Python", "is", "easy"]

print(" ".join(words))
# Output: Python is easy

# 25. ljust()
# Returns a left-justified string.
# The remaining space is filled with the given character.
text = "Python"

print(text.ljust(15, "-"))
# Output: Python---------

# 26. lower()
# Converts all letters to lowercase.
text = "HELLO Python"

print(text.lower())
# Output: hello python

# 27. lstrip()
# Removes whitespace from the LEFT side of the string.
text = "   Hello"

print(text.lstrip())
# Output: Hello

# It can also remove specified characters.
text = "###Hello"
print(text.lstrip("#"))
# Output: Hello

# 28. maketrans()
# Creates a translation table.
# Usually used together with translate()
table = str.maketrans("abc", "123")
text = "abcabc"

print(text.translate(table))
# Output: 123123

# 29. partition()
# Splits the string into THREE parts:
# 1. Before the separator
# 2. Separator itself
# 3. After the separator
text = "Hello Python World"

print(text.partition("Python"))
# Output: ('Hello ', 'Python', ' World')

# 30. replace()
# Replaces one value with another value.
text = "I like Java"

print(text.replace("Java", "Python"))
# Output: I like Python

# You can also specify the number of replacements.
text = "apple apple apple"

print(text.replace("apple", "mango", 2))
# Output: mango mango apple

# 31. rfind()
# Searches for a value and returns the LAST position.
# If not found, returns -1.
text = "Python is easy. Python is powerful."

print(text.rfind("Python"))
# Output: 16

print(text.rfind("Java"))
# Output: -1

# 32. rindex()
# Searches for a value and returns the LAST position.
# If not found, it raises ValueError.
text = "Python is easy. Python is powerful."

print(text.rindex("Python"))
# Output: 16

# Uncomment to see the error:
# print(text.rindex("Java"))
# ValueError

# 33. rjust()
# Returns a right-justified string.
# The remaining space is filled with the given character.
text = "Python"

print(text.rjust(15, "-"))
# Output: ---------Python

# 34. rpartition()
# Splits the string into THREE parts using the LAST
# occurrence of the specified separator.
text = "Python is easy. Python is powerful."

print(text.rpartition("Python"))
# Output: ('Python is easy. ', 'Python', ' is powerful.')

# 35. rsplit()
# Splits a string from the RIGHT side.
# The second argument specifies maximum number of splits.
text = "apple,banana,mango"

print(text.rsplit(","))
# Output: ['apple', 'banana', 'mango']

print(text.rsplit(",", 1))
# Output: ['apple', 'banana,mango']

# 36. rstrip()
# Removes whitespace from the RIGHT side.
text = "Hello   "

print(text.rstrip())
# Output: Hello

# It can also remove specified characters.
text = "Hello###"

print(text.rstrip("#"))
# Output: Hello

# 37. split()
# Splits a string and returns a LIST.
# By default, it splits wherever there is whitespace.
text = "Python is easy"

print(text.split())
# Output: ['Python', 'is', 'easy']
# Using a separator
text = "apple,banana,mango"

print(text.split(","))
# Output: ['apple', 'banana', 'mango']

# Limiting the number of splits
text = "one-two-three-four"

print(text.split("-", 2))
# Output: ['one', 'two', 'three-four']

# 38. splitlines()
# Splits a string at line breaks.
# Returns a LIST.
text = "Hello\nPython\nWorld"
print(text.splitlines())
# Output: ['Hello', 'Python', 'World']

# 39. startswith()
# Returns True if the string starts with the specified value.
text = "Hello Python"

print(text.startswith("Hello"))
# Output: True

print(text.startswith("Python"))
# Output: False

# 40. strip()
# Removes whitespace from BOTH left and right sides.
# It does not remove spaces from the middle.
text = "   Hello World   "

print(text.strip())
# Output: Hello World

# It can also remove specified characters.
text = "###Hello###"

print(text.strip("#"))
# Output: Hello

# 41. swapcase()
# Converts uppercase letters to lowercase
# and lowercase letters to uppercase.

text = "Hello Python"

print(text.swapcase())
# Output: hELLO pYTHON

# 42. title()
# Converts the first character of EACH WORD to uppercase.
text = "hello python programming"

print(text.title())
# Output: Hello Python Programming

# 43. translate()
# Replaces characters according to a translation table.
# Usually used with maketrans().
table = str.maketrans("aeiou", "12345")

text = "hello"

print(text.translate(table))
# Output: h2ll4

# 44. upper()
# Converts all letters to uppercase.
text = "hello Python"

print(text.upper())
# Output: HELLO PYTHON

# 45. zfill()
# Adds zeros to the LEFT side of the string
# until it reaches the specified width.
text = "25"

print(text.zfill(5))
# Output: 00025

text = "123"

print(text.zfill(6))
# Output: 000123