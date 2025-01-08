from itertools import permutations

N = int(input())
li = list(map(int, input().split()))
cases = permutations([i for i in range(1, N+1)], N)

def check_valid_seats(seats) -> bool:
  for height, person_number in enumerate(li, start=1):
    count = 0
    idx = 0
    while idx <= N and not (seats[idx]==height):
      if seats[idx] > height:
        count += 1
      idx += 1

    if count != person_number:
      return False
  return True

for c in cases:
  if check_valid_seats(c):
    break
print(*c)