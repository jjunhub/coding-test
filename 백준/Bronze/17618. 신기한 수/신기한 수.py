N = int(input())

count = 0

for 나눠지는수 in range(1, N+1):
  나눌수 = str(나눠지는수)
  합 = 0
  for 숫자한개 in 나눌수:
    합 += int(숫자한개)
  if 나눠지는수 % 합 == 0:
    count += 1


print(count)