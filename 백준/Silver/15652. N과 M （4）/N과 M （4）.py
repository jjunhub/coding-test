from itertools import combinations_with_replacement

N, M = map(int, input().split())
numbers = [ number for number in range(1, N+1) ]

for el in combinations_with_replacement(numbers, M):
  print(*el)