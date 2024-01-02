class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        beforePrice = prices[0]
        profits = []
        
        for nowPrice in prices:
            if nowPrice > minPrice:
                profits.append(nowPrice - minPrice)
            else :
                minPrice = nowPrice
        
        if profits:
            return max(profits)
        else :
            return 0
            