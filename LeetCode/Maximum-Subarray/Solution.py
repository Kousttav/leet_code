1class Solution:
2    def maxSubArray(self, nums: List[int]) -> int:
3        if not nums:
4            return 0
5        mx=ans=nums[0]
6        for i in range(1,len(nums)):
7            mx=max(nums[i],nums[i]+mx)
8            ans=max(ans,mx)
9        return ans