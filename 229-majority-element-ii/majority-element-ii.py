class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c=len(nums)//3
        d={}
        for n in nums:
            d[n] = d.get(n, 0) + 1
        l=[]
        for i in d:
            if d[i]>c:
                l.append(i)
        return l
        