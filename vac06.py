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

    

