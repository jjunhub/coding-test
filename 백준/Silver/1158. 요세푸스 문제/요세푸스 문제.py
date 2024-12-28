from collections import deque
N, K = map(int, input().split())
q = deque([str(i) for i in range(1, N+1)])
answer = []

while q:
  q.rotate(-(K-1))
  answer.append(q.popleft())

print("<" + ", ".join(answer) +">")