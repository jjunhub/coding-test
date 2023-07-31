import sys
input = sys.stdin.readline

prevSum = 0 # 이전까지의 합을 담은 변수
score = 0 # 100과 가장 가까운 값

for _ in range(10):
  prevSum += int(input())

  if( abs(100-score) >= abs(100-prevSum) ) :
    score = prevSum

print(score)