1class Solution:
2    def countPairs(self, nums: List[int], target: int) -> int:
3        nums.sort()
4        count = 0
5        left = 0
6        right = len(nums)-1
7        while left<right:
8            if nums[left]+nums[right]<target:
9                count+=right-left
10                left +=1
11            else:
12                right-=1
13        return count