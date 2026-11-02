# Read N (positive integer)
n = int(input("Enter N (positive integer): " ))
while n <= 0:
    n = int(input("N must be positive. Enter N again: "))


# Read N numbers, one by one
numbers = []
for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Read X and search for it
x = int(input("Enter X: "))

result = -1
for i in range(n):
    if numbers[i] == x:
        result = i + 1
        break

print(f"The result is {result}")