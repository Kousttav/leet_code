class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=[]
        for i in range(len(nums)):
            if nums[i] == target:
                l.append(i)
        print(l)
        if not l:
            return [-1, -1]
        res=[]
        res.append(l[0])
        res.append(l[-1])
        return res