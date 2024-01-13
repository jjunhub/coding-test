import sys
input = sys.stdin.readline

n = int(input())
li = []

for i in range(1,n+1):
  li.append(i)

while len(li) > 1:
  newLi = []
  for i in range(1, len(li), 2):
    newLi.append(li[i])
  li = newLi

print(li[0])