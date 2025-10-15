def remove_even(numbers):
  """
  Attempts to remove even numbers from a list of integers in-place.

  Args:
    numbers (list): A list of integers from which to remove even numbers.
  """
  # This loop iterates over the actual numbers in the list.
  for i in numbers:
      if i % 2 == 0:
          numbers.remove(i)

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    remove_even(numbers)
    print(numbers)
