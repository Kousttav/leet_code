class Solution:
    def countElements(self, nums: List[int]) -> int:
        s=list(set(nums))
        s.sort()
        c=0
        for i in nums:
            if s.index(i)!=0 and s.index(i)!=len(s)-1:
                c+=1
        return c
        
        