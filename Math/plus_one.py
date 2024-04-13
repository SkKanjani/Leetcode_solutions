
## Problem: https://leetcode.com/problems/plus-one
## Difficulty: Easy
## Solution: 

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in reversed(range(len(digits))):
            if digits[i]==9:
                digits[i]=0
            else:
                digits[i]=digits[i]+1
                return digits
        return [1]+digits