"""
Given an array `nums` of integers, return how many of them contain
and even number of digits.
"""
from timeit import timeit


class Solution:

    def __init__(self, nums: list):
        self.nums = nums

    def even_number_digits(self):
        even_digit_cnt = 0
        for n in self.nums:
            if len(str(n)) % 2 == 0:
                even_digit_cnt += 1
        return even_digit_cnt

    # def even_number_digits_fast(self):
    #     return sum([True for n in self.nums if len(str(n)) % 2 == 0])

    def time_func(self, quick=0):
        time = timeit(lambda: self.even_number_digits())
        print(f'The function even number of digits took {time} seconds')


numbers = [12, 345, 2, 6, 7896]
example = Solution(numbers)
example.time_func()
print(example.even_number_digits())



