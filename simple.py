"""Program to calculate the sum of first N natural numbers."""


def calculate_sum(n):
    """Return the sum of first n natural numbers."""
    return sum(range(1, n + 1))


NUMBER = 10
RESULT = calculate_sum(NUMBER)

print("The total sum is:", RESULT)
