class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l=z=sum=0
        for r in range(0,len(nums)):
            if nums[r]==0:
                z+=1
            while(z>1):
                if nums[l]==0:
                    z-=1
                l+=1
            sum = max(sum,r-l)
        return sum
        