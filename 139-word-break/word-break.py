from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)  # O(1) membership checks
        n = len(s)
        if n == 0:
            return True

        # Optional optimization: avoid building substrings longer than the longest word
        max_len = max((len(w) for w in wordDict), default=0)

        stack = [0]        # start indices to explore
        visited = set()    # start indices already fully explored (cannot lead to solution)

        while stack:
            i = stack.pop()
            if i == n:
                return True     # reached the end -> success
            if i in visited:
                continue

            st = ''
            # build substring incrementally (keeps your style)
            for j in range(i, n):
                # stop if substring length exceeds longest dictionary word
                if max_len and j - i + 1 > max_len:
                    break
                st += s[j]
                if st in word_set:
                    # push the next start index for later exploration
                    stack.append(j + 1)

            visited.add(i)   # mark this start as explored (no successful path found from it)

        return False
