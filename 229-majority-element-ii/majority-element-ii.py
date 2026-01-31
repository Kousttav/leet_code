class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c=len(nums)//3
        d={}
        for n in nums:
            if n in d:
                d[n]=d[n]+1
            else:
                d[n]=1
        l=[]
        for i in d:
            if d[i]>c:
                l.append(i)
        return l
        