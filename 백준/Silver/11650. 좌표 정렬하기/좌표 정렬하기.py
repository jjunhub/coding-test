import sys
input = sys.stdin.readline

N = int(input())
points = []
for _ in range(N):
  point = list(map(int, input().split()))
  points.append(point)


points.sort()
for A,B in points:
  print(A, B)