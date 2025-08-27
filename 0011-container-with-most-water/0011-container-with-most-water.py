class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n - 1
        m = 0
        max_height = max(height)
        while l < r and m < max_height * (r - l):
            width = r - l
            h = min(height[l], height[r])
            m = max(m, width * h)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return m