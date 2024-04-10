
## Problem: https://leetcode.com/problems/longest-common-prefix
## Difficulty: Easy
## Solution: 

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if strs:
            common_prefix = True
            this_turn = ""
            if strs[0]:
                for i in strs[0]:
                    this_turn = this_turn + i
                    for s in strs:
                        if s and s.startswith(this_turn):
                            continue
                        else:
                            common_prefix = False
                            break
                    if common_prefix:
                        prefix = this_turn
                    else:
                        return prefix
        return prefix