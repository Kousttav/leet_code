1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        if len(nums) <= 2:
4            return len(nums)
5        i = 2
6        for j in range(2, len(nums)):
7            if nums[j] != nums[i - 2]:
8                nums[i] = nums[j]
9                i += 1
10        return i