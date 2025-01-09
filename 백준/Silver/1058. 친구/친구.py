from collections import defaultdict, deque

def bfs(start):
  visited = set()
  q = deque()
  q.append((start, 0))
  visited.add(start)

  while q:
    now_node, count = q.popleft()
  
    for next_node in graph[now_node]:
      if next_node not in visited and count < 2:
        q.append((next_node, count+1))
        visited.add(next_node)

  return len(visited)-1

N = int(input())
graph = defaultdict(list)
for one in range(N):
  YN = input()
  for friend_number, is_friend in enumerate(YN):
    if is_friend == "Y":
      graph[one].append(friend_number)

answer = 0
for i in range(N):
  answer = max(answer, bfs(i))
print(answer)