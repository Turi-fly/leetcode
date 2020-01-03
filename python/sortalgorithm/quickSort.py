#!/usr/bin/env python
# -*- coding: utf-8 -*-


class QuickSort:

    """
    快速排序
    """

    def __init__(self):
        pass

    def quicksort(self, nums):
        if len(nums) == 1 or len(nums) == 0:
            return nums

        less = []
        greater = []
        middle_num = nums.pop()

        for num in nums:
            if num > middle_num:
                greater.append(num)
            if num < middle_num:
                less.append(num)
        return self.quicksort(less) + [middle_num] + self.quicksort(greater)


if __name__ == '__main__':
    print(QuickSort().quicksort([5, 6, 1, 3, 4, 2]))
