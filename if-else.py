# If-Else Statement in Python
# Program to check the person is eligible to ride a vehicle based on age
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to ride a vehicle.")
else:
    print("You are not eligible to ride a vehicle.")

# Write a program to find if a number is even or odd using if-else statement
number = int(input("Enter a number: "))
if number % 2 == 0: 
    print("The number is even.")
else:
    print("The number is odd.") 

# write a program to check day according to the number entered by the user using dictionary
day = int(input("Enter a number (1-7) to check the day: "))
days = {1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday", 7:"Sunday"}
if day == 1:
    print("The day is: Monday")
elif day == 2:
    print("The day is: Tuesday")
elif day == 3:
    print("The day is: Wednesday")
elif day == 4:
    print("The day is: Thursday")
elif day == 5:
    print("The day is: Friday")
elif day == 6:
    print("The day is: Saturday")
elif day == 7:
    print("The day is: Sunday")
else:
    print("Invalid input")