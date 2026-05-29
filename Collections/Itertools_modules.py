"""
Demonstration of commonly used itertools functions:
product, permutations, combinations, accumulate, groupby,
count, cycle, and repeat.
"""

from itertools import (
    product,
    permutations,
    combinations,
    combinations_with_replacement,
    accumulate,
    groupby,
    count,
    cycle,
    repeat
)
import operator


# ---------------------------------------------------
# PRODUCT
# ---------------------------------------------------
list_a = [1, 2]
list_b = [4]

# Cartesian product with repeat=2
cartesian_product = product(list_a, list_b, repeat=2)
print("Product:", list(cartesian_product))


# ---------------------------------------------------
# PERMUTATIONS
# ---------------------------------------------------
numbers = [1, 2, 3]

# All permutations of length 3
all_permutations = permutations(numbers)
# permutations(numbers, 2)  # Uncomment for length-2 permutations
print("Permutations:", list(all_permutations))


# ---------------------------------------------------
# COMBINATIONS
# ---------------------------------------------------
values = [1, 2, 3, 4]

two_combinations = combinations(values, 2)
print("Combinations:", list(two_combinations))

# Combinations with replacement
combination_with_replacement = combinations_with_replacement(list_a, 2)
print("Combinations with replacement:", list(combination_with_replacement))


# ---------------------------------------------------
# ACCUMULATE
# ---------------------------------------------------
sequence = [1, 2, 3, 4]

# Default accumulate (addition)
sum_accumulate = accumulate(sequence)
print("Accumulate (sum):", list(sum_accumulate))

# Accumulate using multiplication
product_accumulate = accumulate(sequence, operator.mul)
print("Accumulate (product):", list(product_accumulate))

# Accumulate using max
max_accumulate = accumulate(sequence, max)
print("Accumulate (max):", list(max_accumulate))


# ---------------------------------------------------
# GROUPBY
# ---------------------------------------------------
def is_smaller_than_3(value):
    return value < 3


group_values = [1, 2, 3, 4]
grouped = groupby(group_values, key=is_smaller_than_3)

for key, group in grouped:
    print("Group key:", key, "Values:", list(group))


# ---------------------------------------------------
# COUNT
# ---------------------------------------------------
print("Count:")
for number in count(start=10):
    print(number)
    if number == 15:
        break


# ---------------------------------------------------
# CYCLE (FIXED)
# ---------------------------------------------------
print("Cycle:")
cycle_list = [1, 2, 3]

counter = 0
for item in cycle(cycle_list):
    print(item)
    counter += 1
    if counter == 10:   # prevent infinite loop
        break


# ---------------------------------------------------
# REPEAT (FIXED)
# ---------------------------------------------------
print("Repeat:")
# repeat(value, times)
for item in repeat(1, 5):
    print(item)
