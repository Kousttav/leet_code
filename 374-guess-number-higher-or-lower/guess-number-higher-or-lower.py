class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:
            mid = (left+right) // 2
            g = guess(mid)
            if g == 0:
                return mid
            elif g == 1:
                left = mid+1
            else:
                right = mid-1
        return -1