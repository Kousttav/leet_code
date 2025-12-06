class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        if original not in nums:
            return original
        else:
            t=original
            while(t in nums):
                t=t*2
            print(t)
            return t
            
        