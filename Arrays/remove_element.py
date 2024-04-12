
## Problem: https://leetcode.com/problems/remove-element
## Difficulty: Easy
## Solution: 

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp = []
        for n in nums:
            if n == val:
                continue
            else:
                temp.append(n)
        for i in range(len(temp)):
            nums[i] = temp[i]
        return len(temp)