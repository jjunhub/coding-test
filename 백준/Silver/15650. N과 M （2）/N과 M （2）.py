import itertools

n, r = map(int, input().split())
numbers = [ ]
for num in range(1, n+1):
  numbers.append(num)

for a in itertools.combinations(numbers, r):
  print(*a)