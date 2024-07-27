import sys
from collections import deque
input = sys.stdin.readline

def bfs(start) -> int:
  queue = deque()
  queue.append(start) # ( (행, 열), 거리 )
  dir = [ (1,0), (-1,0), (0, -1), (0, 1) ] # 상하좌우

  while queue:
    cur_v_hang, cur_v_yeol, distance = queue.popleft()

    if cur_v_hang == hang-1 and cur_v_yeol == yeol-1:
      return distance

    for idx in range(4):
      next_v_hang, next_v_yeol = cur_v_hang + dir[idx][0], cur_v_yeol + dir[idx][1]
    
      # matrix 범위를 벗어난 경우
      if not ( 0 <= next_v_hang < hang and 0 <= next_v_yeol < yeol ):
        continue
    
      if matrix[next_v_hang][next_v_yeol] == "1":
        queue.append((next_v_hang, next_v_yeol, distance + 1))
        matrix[next_v_hang][next_v_yeol] = "0"


hang, yeol = map(int, input().split())

matrix = []

for _ in range(hang):
  # 문자열로 입력
  line_str = input().rstrip()
  line_li = []
  
  # 리스트로 변환
  for el in line_str:
    line_li.append(el)
  
  matrix.append(line_li)

print(bfs((0, 0, 1)))