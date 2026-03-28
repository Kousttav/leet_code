1class Solution:
2    def dominantIndex(self, nums: List[int]) -> int:
3        n=max(nums)
4        # for i in nums:
5        # if i != n:
6        # if n>=2*i:
7        if all(n>=2*i for i in nums if i != n):
8            return nums.index(n)
9        return -1