class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        l=set(candyType)
        n=len(candyType)
        r=min(n//2,len(l))
        return r
                