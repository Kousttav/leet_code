class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        t=original
        while(t in nums):
            t=t*2
        return t
            
        