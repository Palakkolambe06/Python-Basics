square = lambda x: x * x

print(square(5))

# Recursion - function again and again calling itself
# write a program to inverse count down

def count_down(n):
    if n == 0:
        print("Done!")
        return
    print(n)
    count_down(n - 1)

count_down(10)

# Write a program to find factorial of a number using recursion - 5*4*3*2*1=5! , factorial of 0 is 1

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)                                 

print(factorial(5))
