class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        profit = 0
        
        for nowPrice in prices:
            if nowPrice > minPrice:
                profit = max(profit, nowPrice-minPrice)
            else :
                minPrice = nowPrice
        
        return profit    