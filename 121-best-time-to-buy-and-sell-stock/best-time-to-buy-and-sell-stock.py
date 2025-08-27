class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p=0
        b=prices[0]
        for s in prices[1:]:
            if s>b:
                p=max(p,s-b)
            else:
                b=s
        return p

        