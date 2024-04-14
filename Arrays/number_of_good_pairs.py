
## Problem: https://leetcode.com/problems/number-of-good-pairs
## Difficulty: Easy
## Solution: 

from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = 0
        for j in range(len(nums)):
            for i in range(j):
                if nums[i] == nums[j]:
                    c += 1
        return c