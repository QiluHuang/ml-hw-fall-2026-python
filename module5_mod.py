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