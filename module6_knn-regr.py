import numpy as np

"""
k-NN Regression on 1-dimensional data using NumPy.

The program:
  1. Reads N (positive integer) - number of training points.
  2. Reads k (positive integer) - number of neighbors.
  3. Reads N (x, y) points one by one (x first, then y). X and Y are real numbers.
  4. Reads a query value X and prints the k-NN Regression result Y
     (the mean of the y-values of the k nearest training points),
     or an error message if k > N.
"""

class KNNRegressor:
    def __init__(self, n_points: int, k: int):
        self.n_points = n_points
        self.k = k
        # Data initialization: pre-allocate NumPy arrays for N points
        self.x = np.zeros(n_points, dtype=float)
        self.y = np.zeros(n_points, dtype=float)
        self._count = 0

    def add_point(self, x_value: float, y_value: float) -> None:
        """Data insertion: place the next (x, y) point into the arrays."""
        if self._count >= self.n_points:
            raise IndexError("All N points have already been inserted.")
        self.x[self._count] = x_value
        self.y[self._count] = y_value
        self._count += 1

    def predict(self, x_query: float) -> float:
        """Data calculation: mean y of the k training points nearest to x_query."""
        if self.k > self.n_points:
            raise ValueError(f"k ({self.k}) must be less than or equal to N ({self.n_points}).")
        # In 1-D, Euclidean (l2) and Manhattan (l1) distances are both |x - x_query|
        distances = np.abs(self.x - x_query)
        # Stable sort so ties are broken by insertion order
        nearest_idx = np.argsort(distances, kind="stable")[: self.k]
        return float(np.mean(self.y[nearest_idx]))


def read_positive_int(prompt: str) -> int:
    """Keep asking until the user enters a positive integer."""
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print("Error: please enter a whole number.")
            continue
        if value <= 0:
            print("Error: the number must be positive.")
            continue
        return value


def read_float(prompt: str) -> float:
    """Keep asking until the user enters a real number."""
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("Error: please enter a real number.")


def main() -> None:
    n = read_positive_int("Enter N (number of points, positive integer): ")
    k = read_positive_int("Enter k (number of neighbors, positive integer): ")

    model = KNNRegressor(n, k)

    for i in range(1, n + 1):
        x_value = read_float(f"Enter x value for point {i}: ")
        y_value = read_float(f"Enter y value for point {i}: ")
        model.add_point(x_value, y_value)

    x_query = read_float("Enter X to predict: ")

    if k <= n:
        y_pred = model.predict(x_query)
        print(f"Result of {k}-NN Regression: Y = {y_pred}")
    else:
        print(f"Error: k ({k}) must be less than or equal to N ({n}). Cannot run k-NN Regression.")

if __name__ == "__main__":
    main()