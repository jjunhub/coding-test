## Before
```python
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
```

## After
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        profit = 0
        
        for nowPrice in prices:
            minPrice = min(minPrice, nowPrice)
            profit = max(profit, nowPrice-minPrice)

        return profit    
```
### 포인트
max, min 함수로 if + 값 치환 과정을 단순화할 수 있다.
