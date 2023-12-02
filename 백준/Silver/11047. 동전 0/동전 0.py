import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
for _ in range(N):
  coins.append(int(input()))

coins.reverse()
coinNumber = 0

for coinValue in coins:
  coinNumber += K // coinValue
  K -= K // coinValue * coinValue

print(coinNumber)