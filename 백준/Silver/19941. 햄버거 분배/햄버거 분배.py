N, K = map(int, input().split())
식탁 = list(input())
count = 0

for 시작위치 in range(N):
  if 식탁[시작위치] == "H" or 식탁[시작위치] == "X":
    continue
  for 자리 in range(max(0, 시작위치-K), min(시작위치+K+1, N)):
    if 식탁[자리] == "H":
      식탁[자리] = "X"
      count +=1
      break

print(count)