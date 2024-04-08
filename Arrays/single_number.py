
## Problem: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/549/
## Difficulty: Easy
## Solution: 

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            c = nums.count(nums[i])
            if c==1:
                return c