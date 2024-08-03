import sys
input = sys.stdin.readline

N = int(input())
costs = []
answer = [[-1,-1,-1] for _ in range(N)]

for _ in range(N):
  R, G, B = map(int, input().split())
  costs.append([R,G,B])

answer[0][0] = costs[0][0]
answer[0][1] = costs[0][1]
answer[0][2] = costs[0][2]

for i in range(1, N):
  answer[i][0] = costs[i][0] + min(answer[i-1][1], answer[i-1][2])
  answer[i][1] = costs[i][1] + min(answer[i-1][0], answer[i-1][2])
  answer[i][2] = costs[i][2] + min(answer[i-1][0], answer[i-1][1])

print(min(answer[N-1]))