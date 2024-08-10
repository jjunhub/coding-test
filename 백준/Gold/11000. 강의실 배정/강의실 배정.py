import sys
from heapq import heapify, heappop, heappush
input = sys.stdin.readline

N = int(input())
candidate_classes = list()
progress_classes = list()
endTime = -1
max_classroom_num = 0

for _ in range(N):
  start, end = map(int, input().split())
  candidate_classes.append((start, end))

candidate_classes.sort() # 시작 시간이 빠를수록 앞에 존재한다.
heapify(progress_classes) # 종료 시간이 빠를수록 앞에 존재한다.

for tick, end in candidate_classes:
  
  while progress_classes and progress_classes[0][0] <= tick: # 과거 수업이 종료되었다면,
      heappop(progress_classes) # 수업중인 반 목록에서 제거
    
  heappush(progress_classes, (end, tick)) # 그리고 수업중인 반 목록으로 전달
  
  max_classroom_num = max(max_classroom_num, len(progress_classes)) # 현재 반 개수 점검

print(max_classroom_num)