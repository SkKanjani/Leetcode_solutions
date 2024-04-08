
## Problem: https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
## Difficulty: Easy
## Solution: 

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0 or n == 1:
            return n
        unique = [0] * n
        count = 0
        for i in range(n-1):
            if nums[i] != nums[i + 1]:
                unique[count] = nums[i]
                count = count + 1
        unique[count] = nums[n - 1]
        count = count + 1
        for i in range(count):
            nums[i] = unique[i]
        return count
