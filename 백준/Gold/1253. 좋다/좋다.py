import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
goodNumbers = []
goodCount = 0

for index, target in enumerate(numbers):
    leftPtr = 0
    rightPtr = len(numbers) - 1
    if leftPtr == index : leftPtr += 1
    if rightPtr == index : rightPtr -= 1

    while(leftPtr < rightPtr):
        temp = numbers[leftPtr] + numbers[rightPtr]
        if ( temp < target ) :
            leftPtr += 1
            if leftPtr == index : leftPtr += 1
        elif ( temp > target ) :
            rightPtr -= 1
            if rightPtr == index : rightPtr -= 1
        else : # temp == target
            goodNumbers.append(target)
            rightPtr -= 1
            if rightPtr == index : rightPtr -= 1

newGoodNumbers = set(goodNumbers)
for number in newGoodNumbers:
    goodCount += numbers.count(number)

print(goodCount)