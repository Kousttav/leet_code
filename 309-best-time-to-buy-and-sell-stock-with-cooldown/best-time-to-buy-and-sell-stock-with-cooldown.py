class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell,prev_sell,buy=0,0,-float('inf')
        for i in range(len(prices)):
            prev_buy=buy
            buy=max(prev_sell-prices[i],prev_buy)
            prev_sell=sell
            sell=max(prev_buy+prices[i],prev_sell)
        return sell



                

        