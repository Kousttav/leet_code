class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n=len(nums)
        c=0
        for i in range(n):
            for j in range(n):
                if i!=j and nums[i] + nums[j]<target:
                    c+=1
        return c//2