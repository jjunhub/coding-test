import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def bfs(start) -> int:
  li = [(start,0)]
  q = deque(li)

  while q:
    now, count = q.popleft()

    if short_cut[now] : # 지름길
      for next in short_cut[now]:
        if memo[next] > count:
          memo[next] = count
          q.append((next, count))
    else : # 주사위
      for i in range(1, 7):
        if now+i <= 100 and memo[now+i] > count:
          memo[now+i] = count + 1
          q.append((now+i, count+1))

ladders, snakes  = map(int, input().split())
short_cut = defaultdict(list)
memo = [100 for _ in range(101)] 

for _ in range(ladders + snakes):
  sc_start, sc_end = map(int, input().split())
  short_cut[sc_start].append(sc_end)

bfs(1)
print(memo[100])