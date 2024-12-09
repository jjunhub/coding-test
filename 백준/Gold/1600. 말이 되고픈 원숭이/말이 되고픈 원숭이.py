from collections import deque
import sys
input = sys.stdin.readline

default_move = [ (0, 1), (0, -1), (1, 0), (-1, 0)]
horse_move = [ (1, -2), (1, 2), (2, -1), (2, 1), (-1, -2), (-1, 2), (-2, -1), (-2, 1) ]

def bfs(start, item):
  
  visited = [[[ 201*201 for item in range(item+1)] for column in range(column)] for row in range(row)]
  q = deque()
  q.append((start, 0, item)) # (h, y), count, item_remain

  while q:
    now_node, count, item_remain = q.popleft()
    now_r, now_c = now_node
    if visited[now_r][now_c][item_remain] <= count:
      continue
    visited[now_r][now_c][item_remain] = count
    
    for dr, dc in default_move:
      next_r, next_c = now_r + dr, now_c + dc
      if not (0 <= next_r < row and 0 <= next_c < column): continue
      if matrix[next_r][next_c] == 1: continue
      
      q.append(((next_r, next_c), count+1, item_remain))
      
    if item_remain > 0:
      for dr, dc in horse_move:
        next_r, next_c = now_r + dr, now_c + dc
        if not (0 <= next_r < row and 0 <= next_c < column): continue
        if matrix[next_r][next_c] == 1: continue
      
        q.append(((next_r, next_c), count+1, item_remain-1))

  answer = min(visited[row-1][column-1])
  if answer == 201*201:
    return -1
  else :
    return answer

K = int(input())
column, row = map(int, input().split())

matrix = []
for _ in range(row):
  line = list(map(int, input().split()))
  matrix.append(line)

start = (0,0)
print(bfs(start, K))