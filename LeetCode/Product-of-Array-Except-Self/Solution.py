1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        if nums.count(0)>=2:
4            return [0]*len(nums)
5        total=1
6        for k in range(len(nums)):
7            total*=nums[k]
8        other=1
9        for i in range(len(nums)):
10            if nums[i]!=0:
11                other*=nums[i]
12        l=[] 
13        for j in range(len(nums)):
14            if nums[j]!=0:
15                l.append(total//nums[j])
16            else:
17                l.append(other)
18        return l
19        