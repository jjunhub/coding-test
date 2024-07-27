from itertools import permutations

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

for el in permutations(numbers, M):
  print(*el)