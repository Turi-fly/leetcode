#!/usr/bin/env python
# -*- coding: utf-8 -*-


class BubbleSort:

    """
    冒泡排序
    """

    def __init__(self):
        pass

    def bubbleSort(self, nums):
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[j] < nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums


if __name__ == '__main__':
    print(BubbleSort().bubbleSort([5, 6, 1, 3, 4, 2]))
