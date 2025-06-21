class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        mx=ans=nums[0]
        for i in range(1,len(nums)):
            mx=max(nums[i],nums[i]+mx)
            ans=max(ans,mx)
        return ans