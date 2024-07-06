import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
matrix = []
for _ in range(N):
  st = input().rstrip()
  li = []
  for apartment in st:
    li.append(int(apartment))
  matrix.append(li)

visited = [[False] * N for _ in range(N)]
answer = []

def bfs(start):
  queue = deque()
  queue.append(start)
  visited[start[0]][start[1]] = True
  answer = 1
  while queue:
    cur_hang, cur_yeol = queue.popleft()

    # 상
    if cur_hang > 0 and matrix[cur_hang-1][cur_yeol] == 1 :
      if visited[cur_hang-1][cur_yeol] == False:
        queue.append((cur_hang-1, cur_yeol))
        visited[cur_hang-1][cur_yeol] = True
        answer +=1 
    
    # 하
    if cur_hang < N-1 and matrix[cur_hang+1][cur_yeol] == 1 :
      if visited[cur_hang+1][cur_yeol] == False:
        queue.append((cur_hang+1, cur_yeol))
        visited[cur_hang+1][cur_yeol] = True
        answer +=1

    # 좌
    if cur_yeol > 0 and matrix[cur_hang][cur_yeol-1] == 1 :
      if visited[cur_hang][cur_yeol-1] == False:
        queue.append((cur_hang, cur_yeol-1))
        visited[cur_hang][cur_yeol-1] = True
        answer +=1

    # 우
    if cur_yeol < N-1 and matrix[cur_hang][cur_yeol+1] == 1 :
      if visited[cur_hang][cur_yeol+1] == False:
        queue.append((cur_hang, cur_yeol+1))
        visited[cur_hang][cur_yeol+1] = True
        answer +=1 

  return answer

for hang in range(N):
  for yeol in range(N):
    if matrix[hang][yeol] == 1 and visited[hang][yeol] == False:
      answer.append(bfs((hang, yeol)))


print(len(answer))
answer.sort()
for a in answer:
  print(a)