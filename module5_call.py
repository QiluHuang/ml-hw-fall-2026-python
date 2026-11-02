from module5_mod import NumberList

# Read N (positive integer)
n = int(input("Enter N (positive integer): "))
while n <= 0:
    n = int(input("N must be positive. Enter N again: "))

# Read N numbers, one by one
number_list = NumberList()
for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    number_list.insert(num)

# Read X and search for it
x = int(input("Enter X: "))
print(number_list.search(x))