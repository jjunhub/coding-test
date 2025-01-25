from itertools import combinations

# 입력
N, M = map(int, input().split())
matrix = []
chickens = set()
houses = set()

# 치킨집, 집 위치 계산
for row in range(N):
  line = list(map(int, input().split()))
  for col, val in enumerate(line):
    if val == 2: # Chicken!
      chickens.add((row, col))
    elif val == 1: # home
      houses.add((row, col))
  matrix.append(line)

# 거리 계산 함수
def get_chicken_distance(house, chickens) -> int:
  min_chicken_distance = 101
  for chicken in chickens:
    min_chicken_distance = min(min_chicken_distance, abs(chicken[0]-house[0]) + abs(chicken[1]-house[1]) )
  return min_chicken_distance

answer = 100 * 13
# 폐업시키지 않을 치킨집을 M개 선택 ( 반복 )
for alive_chiken in combinations(chickens, M):
  # 해당 케이스에 대한 치킨 거리 최소값 계산
  temp_answer = 0
  for house in houses:
    temp_answer += get_chicken_distance(house, alive_chiken)
  
  # 비교
  answer = min(answer,  temp_answer)

# 정답 출력
print(answer)