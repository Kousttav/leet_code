class Solution:
    def addRungs(self, rungs: list[int], dist: int) -> int:
        ans = 0
        prev = 0

        for rung in rungs:
            gap = rung - prev

            if gap > dist:
                ans += (gap - 1) // dist

            prev = rung

        return ans