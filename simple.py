"""Program to calculate the sum of first N natural numbers."""


def calculate_sum(n):
    """Return the sum of first n natural numbers."""
    return sum(range(1, n + 1))


number = 10
result = calculate_sum(number)

print("The total sum is:", result)
