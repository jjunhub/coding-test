from itertools import combinations

N, target = map(int, input().split())
numbers = list(map(int, input().split()))
count = 0

for a in range(1, 21):
  numbers_comb = list(combinations(numbers, a))
  for numbers_one in numbers_comb:
    if sum(numbers_one) == target:
      count += 1

print(count)