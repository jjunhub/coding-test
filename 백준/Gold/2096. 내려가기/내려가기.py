import sys
input = sys.stdin.readline

N = int(input())
dp_max = [0, 0, 0]
dp_min = [0, 0, 0]

for row in range(0, N):
  matrix = list(map(int, input().split()))
  dp_max[0], dp_max[1], dp_max[2] = matrix[0] + max(dp_max[0], dp_max[1]), matrix[1] + max(dp_max[0], dp_max[1], dp_max[2]), matrix[2] + max(dp_max[1], dp_max[2])
  dp_min[0], dp_min[1], dp_min[2] = matrix[0] + min(dp_min[0], dp_min[1]), matrix[1] + min(dp_min[0], dp_min[1], dp_min[2]), matrix[2] + min(dp_min[1], dp_min[2])

print(max(dp_max), min(dp_min))