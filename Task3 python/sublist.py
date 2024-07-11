def has_zero_sum_sublist(arr):
    """
    Check if there is a sublist with sum equal to zero.
    
    :param arr: List of integers.
    :return: True if there is a sublist with sum equal to zero, else False.
    """
    cumulative_sum = 0
    cumulative_sum_set = set()

    for num in arr:
        cumulative_sum += num

        # Check if cumulative sum is zero or already exists in the set
        if cumulative_sum == 0 or cumulative_sum in cumulative_sum_set:
            return True

        cumulative_sum_set.add(cumulative_sum)

    return False

# Example usage
arr = [4, 2, -3, 1, 6]
result = has_zero_sum_sublist(arr)

if result:
    print("There is a sublist with sum equal to zero.")
else:
    print("There is no sublist with sum equal to zero.")
