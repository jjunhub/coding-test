from itertools import permutations

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

answer = []
for el in permutations(numbers, M):
  answer.append(el)

for el in sorted(list(set(answer))):
  print(*el)