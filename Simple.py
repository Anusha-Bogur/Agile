"""Program to calculate the sum of first N natural numbers"""

number = int(input("Enter a number: "))

total = 0

for i in range(1, number + 1):
    total += i

print("The total sum is:", total)
