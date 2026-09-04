1class Solution:
2    def countPairs(self, nums: List[int], target: int) -> int:
3        n=len(nums)
4        c=0
5        for i in range(n):
6            for j in range(n):
7                if i!=j and nums[i] + nums[j]<target:
8                    c+=1
9        return c//2