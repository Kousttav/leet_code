class Solution:
    def maxSum(self, nums: List[int]) -> int:
        s=0
        for n in set(nums):
            if n>0:
                s+=n
        if s==0:
            return max(nums)
        return s  

