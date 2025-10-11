from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)            # O(1) lookups
        n = len(s)
        memo = {}                           

        def can_break(i: int) -> bool:
            if i == n:
                return True
            if i in memo:
                return memo[i]

            st = ''
            # build substring incrementally (keeps your style)
            for j in range(i, n):
                st += s[j]
                if st in word_set:
                    if can_break(j + 1):
                        memo[i] = True
                        return True

            memo[i] = False
            return False

        return can_break(0)
