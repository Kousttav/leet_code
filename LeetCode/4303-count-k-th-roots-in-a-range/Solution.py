class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        if k == 1:
            return r - l + 1

        count = 0
        x = 0

        while x ** k <= r:
            if x ** k >= l:
                count += 1
            x += 1

        return count