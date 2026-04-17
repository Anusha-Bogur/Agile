"""Program to calculate the sum of first N natural numbers"""

def calculate_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


number = 10
result = calculate_sum(number)

print("The total sum is:", result)
