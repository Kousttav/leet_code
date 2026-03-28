class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        l=set(candyType)
        n=len(candyType)//2
        return min(n,len(l))
                