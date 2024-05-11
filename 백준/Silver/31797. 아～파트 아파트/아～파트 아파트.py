from collections import defaultdict

N, M = map(int,input().split())

handList = []
dct = defaultdict(int)
for i in range(M):
  a, b = map(int,input().split())
  dct[a] = i+1
  dct[b] = i+1
  handList.append(a)
  handList.append(b)

handList.sort()
print(dct[handList[ (N-1) % len(handList)]])