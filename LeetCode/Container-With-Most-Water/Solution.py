1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        n = len(height)
4        l = 0
5        r = n - 1
6        m = 0
7        max_height = max(height)
8        while l < r and m < max_height * (r - l):
9            width = r - l
10            h = min(height[l], height[r])
11            m = max(m, width * h)
12            if height[l] < height[r]:
13                l += 1
14            else:
15                r -= 1
16        return m