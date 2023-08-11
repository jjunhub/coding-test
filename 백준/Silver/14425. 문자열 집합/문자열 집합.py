import sys
input = sys.stdin.readline

N, M = map(int, input().split())
_set = {}
count = 0

for _ in range(N):
    _set[input().rstrip()] = 0

for _ in range(M):
    if _set.get(input().rstrip(), -1) != -1:
        count += 1

print(count)
        