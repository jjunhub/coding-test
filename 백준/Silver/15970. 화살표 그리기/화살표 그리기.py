import sys
input = sys.stdin.readline
from itertools import combinations

N = int(input())
points = {}

for _ in range(N):
  x, color = map(int, input().split())
  if color not in points:
    points[color] = [x]
  else :
    points[color].append(x)

mySum = 0
for value in points.values():
  value.sort()
  for index in range(len(value)):
    if index == 0:
      mySum += value[1] - value[0]
    elif index == len(value)-1:
      mySum += value[-1] - value[-2]
    else :
      if value[index+1] - value[index] < value[index] - value[index-1]:
        mySum += value[index+1] - value[index]
      else :
        mySum += value[index] - value[index-1]
 
print(mySum)