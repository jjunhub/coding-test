import sys
input = sys.stdin.readline

n = int(input())
crosswalk = list(map(int,input().split()))
left = list(map(int,input().split()))

leftSum = [0] # leftSum[i] = sum(left[0:i])
rightSum = [0]
temp = 0
for i in left :
    temp += i
    leftSum.append(temp)

right = list(map(int,input().split()))
temp = 0
for i in right :
    temp += i
    rightSum.append(temp)

minLen = crosswalk[0] + rightSum[-1]
minIndex = 1
for index, crosswalkLength in enumerate(crosswalk):
    tempSum = leftSum[index] + crosswalkLength + (rightSum[-1] - rightSum[index])
    if minLen > tempSum :
        minLen = tempSum
        minIndex = index + 1

print(minIndex, minLen)