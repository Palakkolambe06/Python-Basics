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