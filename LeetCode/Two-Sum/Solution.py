1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        l=[]
4        for i in range(len(nums)):
5            for j in range(i+1,len(nums)):
6                if nums[i]+nums[j]==target:
7                    l.append(i)
8                    l.append(j)
9        return list(set(l))
10
11
12
13        