1class Solution:
2    def searchRange(self, nums: List[int], target: int) -> List[int]:
3        l=[]
4        for i in range(len(nums)):
5            if nums[i] == target:
6                l.append(i)
7        print(l)
8        if not l:
9            return [-1, -1]
10        res=[]
11        res.append(l[0])
12        res.append(l[-1])
13        return res