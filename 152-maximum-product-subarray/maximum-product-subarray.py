class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        mx=mn=ans=nums[0]
        for i in range(1,len(nums)):
            if nums[i]<0:
                mx,mn=mn,mx
            mx=max(nums[i],nums[i]*mx)
            mn=min(nums[i],nums[i]*mn)
            ans=max(ans,mx)
        return ans



        