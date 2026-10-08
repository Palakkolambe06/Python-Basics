a = [1, 2, 3, 4, 5, 6]
total = 0

for i in range(len(a)):
    if i % 2 == 0:
        total += i

print("The sum is:", total)

'''
for i in range ( 0, len(a), 2) # 2 is step here - how much forward it had to go.

'''
# factorial - 5*4*3*2*1
n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i

print("The factorial is:", factorial)

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


