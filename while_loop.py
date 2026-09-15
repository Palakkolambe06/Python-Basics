correct_pass = "somepassword"
not_correct_pass = "wrongpassword"
while True:
    password = input("Enter the password: ")
    if password == correct_pass:
        print("Access granted")
        break
    elif password == not_correct_pass:
        print("Access denied")
    else:
        print("Invalid password. Please try again.")

i = 1
while i <= 10:
    print(i)
    i += 1

i = 1

while i <= 10:
    print("The Table of 2 is:")
    print("2 x", i, "=", 2 * i)
    i += 1

i=0
while i <= 10:
    if i== 5:
        i += 1
        continue
    print(i)
    i += 1