from collections import deque


N, M = map(int, input().split())
deq = deque()
answer = 0

for i in range(1, N+1):
  deq.append(i)

pickNumbers = list(map(int, input().split()))
for number in pickNumbers:
  toMove = deq.index(number)
  leftCost = len(deq) - toMove
  rightCost = toMove

  if leftCost < rightCost:
    dir = 1
  else :
    dir = -1

  while deq[0] != number:
    deq.rotate(dir)
    answer += 1
  deq.popleft()

print(answer)