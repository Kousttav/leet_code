class Solution:
    def maximumCandies(self, candies, k: int) -> int:
        left, right = 1, max(candies)
        result = 0
        
        while left <= right:
            mid = left + (right - left) // 2
            c = 0

            for candy in candies:
                c += candy // mid

            if c >= k:
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return result
