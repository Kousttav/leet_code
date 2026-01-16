class Solution:
    def findLucky(self, arr: List[int]) -> int:
        m = -1
        for x in arr:
            if x == arr.count(x):
                m = max(m, x)
        return m
