class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        n=max(nums)
        # for i in nums:
        # if i != n:
        # if n>=2*i:
        if all(n>=2*i for i in nums if i != n):
            return nums.index(n)
        return -1