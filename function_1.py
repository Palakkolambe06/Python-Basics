def great():
    print("Hello, World!")

great()
great()
great()

# inbuilt function
def add(a, b):
    print("The sum is:", a + b)
add(5, 10)

def pi(a):
    print("The value of pi is:", a)
    return(3.14)

pi(3.14)

def greet(name="Student"):
    print("Hello,", name)
greet("Alice")
greet()
greet("Bob")
greet()

def square (n):
    return n * n
print(square(5))

# Design a simple calculator using functions
# Calculator using functions

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == "1":
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == "2":
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == "3":
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == "4":
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid input")