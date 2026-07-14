1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        lookup = {}
4        for i, num in enumerate(nums):
5            if target - num in lookup:
6                return [lookup[target - num], i]
7            lookup[num] = i
8        return []
9
10
11
12        