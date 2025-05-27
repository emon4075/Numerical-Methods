"""
    Generate one thousand random numbers, each with five decimal places.    Calculate the sum of these numbers in three different ways: in the original order, in ascending order, and in descending order, using Python.
"""

import numpy as np

np.random.seed(20250527)

random_numbers = np.round(np.random.random(1000), 5)

sum_original = sum(random_numbers)
print(f"Sum in original order: {sum_original}")
print()

ascending_numbers = sorted(random_numbers)
sum_ascending = sum(ascending_numbers)
print(f"Sum in ascending order: {sum_ascending}")
print()

descending_numbers = sorted(random_numbers, reverse=True)
sum_descending = sum(descending_numbers)
print(f"Sum in descending order: {sum_descending}")
print()

print("Comparison of sums:")
print(f"Original vs Ascending: {sum_original - sum_ascending}")
print(f"Original vs Descending: {sum_original - sum_descending}")
print(f"Ascending vs Descending: {sum_ascending - sum_descending}")

np_sum = np.sum(random_numbers)
print(f"\nNumPy sum (higher precision): {np_sum}")
print(f"Difference between regular sum and NumPy sum: {sum_original - np_sum}")
