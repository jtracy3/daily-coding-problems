"""
Given an array of integers, return indices of the two numbers
such that they add up to a specific target.

You may assume each input would have exactly one solution, and
you may not use the same element twice.
"""
import timeit


def two_sums(numbers: list, target: int):
    """
    Find sum of current number and remaining number

    Parameters
    ----------
        numbers (list): a list of numbers
        target (int): the value we're looking for

    Return
    ------
        indices (list): list of indices from original list that add to the target
    """
    nums_copy = nums.copy()
    for i in range(len(numbers)):
        val = nums_copy.pop(0)
        if not nums_copy:
            return print("Target can't be computed with numbers")
        idx = i
        for j in range(len(nums_copy)):
            sum_ = val + nums_copy[j]
            idx += 1
            if sum_ == target:
                return [i, idx]


def two_sums_hash(numbers: list, target: int):
    hash_table = {}
    for i, num in enumerate(numbers):
        if target - num in hash_table:
            return hash_table[target - num], i
        hash_table[num] = i


def time_func():
    n = [1, 3, 3, 4, 6]
    t = 10
    return timeit.timeit(lambda: two_sums(n, t))


def time_func_hash():
    n = [1, 3, 3, 4, 6]
    t = 10
    return timeit.timeit(lambda: two_sums_hash(n, t))


if __name__ == "__main__":
    nums = [1, 3, 3, 4, 6]
    target_val = 10

    print(f'The two_sums_brute function took {round(time_func(), 4)} seconds to run 1,000,000 times')
    print(two_sums(nums, target_val))
    print('\n')
    print(f'The two_sums_hash function took {round(time_func_hash(), 4)} seconds to run 1,000,000 times')
    print(two_sums_hash(nums, target_val))