
## Problem: https://leetcode.com/problems/palindrome-number/description/
## Difficulty: Easy
## Solution: 

class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        return y==y[::-1]