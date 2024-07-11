def find_duplicates(list1, list2, list3):
    """Find duplicates in three lists."""
    # Convert lists to sets to find common elements
    set1, set2, set3 = set(list1), set(list2), set(list3)
    
    # Find intersection of three sets
    common_elements = set1 & set2 & set3
    
    # Convert set to list for the result
    return list(common_elements)

# Example usage
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
list3 = [5, 6, 10, 11, 12]

duplicates = find_duplicates(list1, list2, list3)
print(f"Common duplicates in the three lists: {duplicates}")
