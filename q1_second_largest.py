def secondLargest(int_list):
    """
    Finds the second largest number in a list of integers.

    Args:
        int_list (list): A list of integers to search through.
                         Example: [10, 5, 8, 20, 3]

    Returns:
        int or None: The second largest integer in the list.
                     Returns None if the list has fewer than two unique values.

    """
    largest = int_list[0]
    second_largest = float("-inf")
    for nos in int_list:
        if nos > largest:
            second_largest = largest
            largest = nos
        elif nos > second_largest and nos != largest:
            second_largest = nos
    return second_largest if second_largest != float("-inf") else None

if __name__ == "__main__":
    numbers = [10, 2, 3, 4, 5]
    print(secondLargest(numbers))
