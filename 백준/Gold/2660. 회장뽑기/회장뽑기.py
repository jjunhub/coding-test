import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def bfs(start):
  visited = set()
  q = deque([(start, 0)])
  visited.add(start)
  while q:
    current_node, score = q.popleft()

    for next_node in graph[current_node]:
      if next_node not in visited:
        visited.add(next_node)
        q.append((next_node, score+1))
  return score

graph = defaultdict(list)
chairman_list = []
chairman_score = 51

number_of_member = int(input())
while True:
  mem1, mem2 = map(int, input().split())
  if mem1 == -1 and mem2 == -1:
    break
  graph[mem1].append(mem2)
  graph[mem2].append(mem1)

for mem in range(1, number_of_member+1):
  score = bfs(mem)
  if score < chairman_score:
    chairman_score = score
    chairman_list = [mem]
  elif score == chairman_score:
    chairman_list.append(mem)

print(chairman_score, len(chairman_list))
print(*chairman_list)