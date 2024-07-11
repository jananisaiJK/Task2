"""

Happy numbers

"""


def is_happy(n):
    """Check if a number is a happy number."""
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1

# Given list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# List to hold happy numbers
happy_numbers = []

# Counting happy numbers
for number in numbers:
    if is_happy(number):
        happy_numbers.append(number)

# Count of happy numbers
happy_count = len(happy_numbers)

# Output results
print(f"Happy numbers: {happy_numbers}")
print(f"Count of happy numbers: {happy_count}")
