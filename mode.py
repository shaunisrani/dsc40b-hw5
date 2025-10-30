# 40b hw 5

def mode(numbers):

  """
  Calculates a mode of a list of numbers.

  A mode is an element that occurs with the greatest frequency.
  This function achieves an average-case time complexity of O(n) by using a
  dictionary to store frequencies. If multiple modes exist, this function
  returns one of them.

  Args:
    numbers: A list of numbers. The numbers can be non-integers and
             non-positive.

  Returns:
    A mode of the list. Returns None if the input list is empty.
  """

  if not numbers:
    return None

  # Step 1: Count the frequency of each number.
  # This pass takes O(n) average-case time because dictionary insertions/accesses
  # are O(1) on average.

  counts = {}
  for num in numbers:
    counts[num] = counts.get(num, 0) + 1

  # Step 2: Find the number with the highest frequency.
  # This pass takes O(k) time, where k is the number of unique elements (k <= n).

  max_count = 0
  result_mode = None # Can be initialized with any element, e.g., numbers[0]

  for num, count in counts.items():
    if count > max_count:
      max_count = count
      result_mode = num

  return result_mode

# --- Example Usage ---
collection1 = [4, 5, 8, 3, 4, 2, 4, 5, 5, -2]
print(f"A mode of the collection is: {mode(collection1)}")
# Expected output: 4 or 5

collection2 = [1, 2, 3, 4, 5]
print(f"A mode of the collection is: {mode(collection2)}")
# Expected output could be any of the elements.

collection3 = []
print(f"A mode of the collection is: {mode(collection3)}")
# Expected output: None