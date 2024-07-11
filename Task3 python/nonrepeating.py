def first_non_repeating_element(arr):
    
    """Find the first non-repeating element in a given list of integers."""
    element_count = {}

    # Count occurrences of each element
    for num in arr:
        if num in element_count:
            element_count[num] += 1
        else:
            element_count[num] = 1

    # Find the first element with a count of 1
    for num in arr:
        if element_count[num] == 1:
            return num

    return None  # Return None if there is no non-repeating element

# Example usage
arr = [9, 4, 9, 6, 7, 4]
result = first_non_repeating_element(arr)
print(f"The first non-repeating element is: {result}")
