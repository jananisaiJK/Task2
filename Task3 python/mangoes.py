def min_difference_of_mangoes(mangoes, m):
    """
    Find the minimum difference between the maximum and minimum mangoes in any subset of m bags.
    
    :param mangoes: List of integers representing mangoes in each bag.
    :param m: Number of students (hence number of bags to consider).
    :return: Minimum difference between the maximum and minimum number of mangoes in any subset of m bags.
    """
    # Sort the list of mangoes
    mangoes.sort()

    # Initialize the minimum difference to a large value
    min_diff = float('inf')

    # Iterate through the sorted list to find the minimum difference
    for i in range(len(mangoes) - m + 1):
        current_diff = mangoes[i + m - 1] - mangoes[i]
        min_diff = min(min_diff, current_diff)

    return min_diff

# Example usage
mangoes = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
m = 7
result = min_difference_of_mangoes(mangoes, m)
print(f"The minimum difference is: {result}")
