N = int(input())
li = [ ]
result = [0] * (N+1)

for i in range(N):
  T, P = map(int, input().split())
  li.append((T, P))

for day, tup in enumerate(li):
  t = tup[0]
  p = tup[1]
  temp = result[day] + p
  if (day + t <= N and result[day + t] < temp):
    result[day+t] = temp
  
  for d in range(day+t, N+1):
    result[d] = max(temp, result[d])

print(max(result))