def find_min_in_rotated_sorted_list(arr):
    """
    Find the minimum element in a rotated sorted list.
    
    :param arr: List of integers which is rotated and sorted.
    :return: The minimum element in the list.
    """
    if not arr:
        return None
    
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        # If mid element is greater than the rightmost element, the minimum is in the right half
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid  # Minimum is in the left half including mid
    
    # At the end of loop, left == right and pointing to the minimum element
    return arr[left]

# Example usage
arr = [4, 5, 6, 7, 0, 1, 2]
result = find_min_in_rotated_sorted_list(arr)
print(f"The minimum element in the rotated sorted list is: {result}")
