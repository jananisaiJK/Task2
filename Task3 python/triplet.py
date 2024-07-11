def find_triplet(arr, target_sum):
    """
    Find a triplet in the list that sums up to the target sum.
    
    :param arr: List of integers.
    :param target_sum: The target sum for the triplet.
    :return: A tuple of the triplet if found, else None.
    """
    n = len(arr)
    arr.sort()  # Sort the array to use the two-pointer technique

    for i in range(n - 2):
        left = i + 1
        right = n - 1
        
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            
            if current_sum == target_sum:
                return (arr[i], arr[left], arr[right])
            elif current_sum < target_sum:
                left += 1
            else:
                right -= 1
                
    return None  # Return None if no triplet is found

# Example usage
arr = [10, 20, 30, 9]
target_sum = 59
result = find_triplet(arr, target_sum)

if result:
    print(f"Triplet found: {result}")
else:
    print("No triplet found")
