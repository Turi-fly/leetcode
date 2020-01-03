#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    """
    给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
    你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素
    """

    def __init__(self):
        pass

    def twoSum1(self, nums, target):
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    def twoSum2(self, nums, target):
        sortid = range(len(nums))
        sortids = sorted(sortid, key=lambda x: nums[x])
        head = 0
        tail = len(nums) - 1
        sumres = nums[sortids[head]] + nums[sortids[tail]]
        while sumres != target:
            if sumres < target:
                head += 1
            if sumres > target:
                tail -= 1
            sumres = nums[sortids[head]] + nums[sortids[tail]]

        return [sortids[head], sortids[tail]]

    def twoSum3(self, nums, target):
        hashmap = {}
        for i, v in enumerate(nums):
            key = target - v
            if key in hashmap:
                return [hashmap[key], i]
            hashmap[v] = i
        return []


if __name__ == '__main__':
    print(Solution().twoSum3([3, 2, 4], 6))
