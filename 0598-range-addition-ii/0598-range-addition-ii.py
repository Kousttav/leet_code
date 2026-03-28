class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        l1=m
        l2=n

        for a,b in ops:
            l1=min(l1,a)
            l2=min(l2,b)
        return l1*l2