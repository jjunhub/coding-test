N = int(input())
primeNum = { i for i in range(3, N+1, 2)}
primeNum.add(2)

for start in range(3, int(N ** 0.5) + 1):
  if start not in primeNum : continue
  for num in range(start * 2, N+1, start):
    primeNum.discard(num)

primeNumList = list(primeNum)
primeNumList.sort()

answer = 0
leftPtr = 0
rightPtr = 0
hap = primeNumList[0]
numberOfprimeNum = len(primeNumList)

while True:
  if hap == N:
    answer += 1

  if hap > N :
    hap -= primeNumList[leftPtr]
    leftPtr += 1
    if leftPtr > numberOfprimeNum-1: break

  else : # hap <= N
    rightPtr += 1
    if rightPtr > numberOfprimeNum-1: break
    hap += primeNumList[rightPtr]

print(answer)