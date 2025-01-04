X = list(input())
X = list(map(int, X))

count = 0
while len(X)>1:
  hap = sum(X)
  count +=1
  X = list(str(hap))
  X = list(map(int, X))
  if hap < 10:
    break

print(count)
if X[0] in [3,6,9]:
  print("YES")
else:
  print("NO")