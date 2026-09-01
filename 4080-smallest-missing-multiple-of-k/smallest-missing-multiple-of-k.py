class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        f=0
        idx=1
        v=0
        while f!=1:
            v=k*idx
            print(v)
            if v not in nums:
                f=1
                return(k*idx)
            idx+=1