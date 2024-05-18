N = int(input())
리스트 = list(map(int, input().split())) # N
부분합 = []
tempHap = 0
hap = 0

for num in 리스트: # N
  tempHap += num
  부분합.append(tempHap)

# FBee SBee 꿀 : 중간 벌(bee)가 이동
for bee in range(1, N-1):
  FBee = 부분합[N-1] - 리스트[0] - 리스트[bee]
  SBee = 부분합[N-1] - 부분합[bee]
  hap = max(hap, FBee + SBee)

# case 꿀 FBee SBee : 중간 벌(bee)가 이동
for bee in range(1, N-1):
  FBee = 부분합[bee-1]
  SBee = 부분합[N-2]-리스트[bee]
  hap = max(hap, FBee + SBee)

# case FBee 꿀 SBee : 중간 꿀(honey)가 이동
for honey in range(1,N-1):
  FBee = 부분합[honey]-리스트[0]
  SBee = 부분합[N-2]-부분합[honey-1]
  hap = max(hap, FBee + SBee)

print(hap)