

# Given list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# List to hold prime numbers
prime_numbers = []

# Counting prime numbers
for number in numbers:
    if is_prime(number):
        prime_numbers.append(number)

# Count of prime numbers
prime_count = len(prime_numbers)

# Output results
print(f"Prime numbers: {prime_numbers}")
print(f"Count of prime numbers: {prime_count}")
