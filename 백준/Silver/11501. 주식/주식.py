import sys
input = sys.stdin.readline

def get_max_benefit(stock_prices : list) -> int: 
  max_temp_price = -1
  benefit = 0
  while stock_prices: # 거꾸로 하나씩
    stock_price = stock_prices.pop()
    if max_temp_price < stock_price:
      max_temp_price = stock_price
    else :
      benefit += (max_temp_price - stock_price)
  return benefit
  
T = int(input())
for _ in range(T):
  days = int(input())
  stock_prices = list(map(int, input().split()))
  print(get_max_benefit(stock_prices))