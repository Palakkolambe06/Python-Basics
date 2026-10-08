# Ugly number
# An ugly number is a positive integer whose only prime factors are 2, 3, or 5.

def is_ugly(n):
    if n <= 0:
        return False

    while n % 2 == 0:
        n //= 2
    while n % 3 == 0:
        n //= 3
    while n % 5 == 0:
        n //= 5

    return n == 1

num = int(input("Enter a number: "))
if is_ugly(num):
    print(num, "is an ugly number")
else:
    print(num, "is not an ugly number") 


