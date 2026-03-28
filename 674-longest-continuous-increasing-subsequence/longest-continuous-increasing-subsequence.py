class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n=len(nums)
        l=1
        c=1
        for i in range(1,n):
            if nums[i] > nums[i-1]:
                c+=1
                l=max(c,l)
            else:
                c=1
        return l