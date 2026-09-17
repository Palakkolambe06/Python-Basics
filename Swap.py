# Write a program to swap two variables without a third variable,
# using arithmetic operations
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
print("Before swap:")
print("a =", a)
print("b =", b)
a = a + b
b = a - b
a = a - b
print("After swap:")
print("a =", a)
print("b =", b)