
## Problem: https://leetcode.com/problems/valid-parentheses
## Difficulty: Easy
## Solution: 

from typing import List

opening_brackets = ['(', '[', '{']
closing_brackets = [')', ']', '}']

class Solution:
    def getOpeningBracket(self, b: str) -> str:
        return opening_brackets[closing_brackets.index(b)]

    def isValid(self, s: str) -> bool:
        st = []
        for i in s:
            if i in opening_brackets:
                st.append(i)
            elif i in closing_brackets:
                if not st:
                    return False
                elif st[-1]==self.getOpeningBracket(i):
                    st.pop(-1)
                else:
                    break
            else:
                break
        if st:
            return False
        else:
            return True