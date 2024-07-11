""""
First and last number of integer
"""
def first_and_last_digit(n):
    """Return the first and last digit of an integer."""
    n_str = str(abs(n))  # Convert to string and handle negative numbers
    first_digit = int(n_str[0])
    last_digit = int(n_str[-1])
    return first_digit, last_digit

# Example usage
number = 501
first_digit, last_digit = first_and_last_digit(number)
print(f"First digit: {first_digit}")
print(f"Last digit: {last_digit}")
