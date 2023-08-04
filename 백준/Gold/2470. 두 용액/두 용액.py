import sys
input = sys.stdin.readline

N = int(input())
solutions = list(map(int, input().split()))
solutions.sort() # Make ascending

leftPtr = 0
rightPtr = len(solutions) - 1

smallValue = solutions[0]
bigValue = solutions[-1]
minDiff = abs(smallValue + bigValue)

while(leftPtr < rightPtr):
    smallTemp = solutions[leftPtr]
    bigTemp = solutions[rightPtr]
    attrTemp = smallTemp + bigTemp

    if attrTemp < 0 :
       leftPtr += 1
    elif attrTemp > 0 :
       rightPtr -= 1
    else : # find solution
       minDiff = 0
       smallValue = smallTemp
       bigValue = bigTemp
       break
       
    if minDiff > abs(attrTemp) : # closer to 0 == abs is smaller
      minDiff = abs(attrTemp)
      smallValue = smallTemp
      bigValue = bigTemp

print(smallValue, bigValue)    