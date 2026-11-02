class NumberList:
    """Stores numbers and finds the position of a given number."""

    def __init__(self):
        # Data initialization: start with an empty list
        self.numbers = []

    def insert(self, num):
        # Data insertion: add a number to the end of the list
        self.numbers.append(num)

    def search(self, x):
        # Data search: return the index (1 to N) of the first X, or -1 if not found
        for i in range(len(self.numbers)):
            if self.numbers[i] == x:
                return i + 1
        return -1


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