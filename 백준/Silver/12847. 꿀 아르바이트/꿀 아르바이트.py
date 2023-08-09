import sys
input = sys.stdin.readline

n, m = map(int, input().split())
infos = list(map(int, input().split()))

maxProfit = sum(infos[:m])
tempProfit = maxProfit
leftPtr = -1
rightPtr = m - 1

while(rightPtr < n - 1):
    leftPtr += 1
    rightPtr += 1
    beforeInfo = infos[leftPtr]
    newInfo = infos[rightPtr]
    tempProfit = tempProfit - beforeInfo + newInfo

    if maxProfit < tempProfit:
        maxProfit = tempProfit

print(maxProfit)