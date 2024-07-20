import sys
from collections import deque
input = sys.stdin.readline

def find_max_pri(q) -> int:
  max_pri = -1
  for _, prior, _ in q:
    max_pri = max(max_pri, prior)
  return max_pri

def find_doc_count(q : deque) -> int:
  count = 1
  while q:
    now_pos, now_prior, flag = q.popleft()
    if now_prior >= find_max_pri(q):
      if flag == True:
        return count
      else :
        count += 1
    else :
      q.append((now_pos, now_prior, flag))

testcase = int(input())
for _ in range(testcase):
  num_of_doc, target_doc_loc = map(int, input().split())
  prior_li = list(map(int, input().split()))
  q = deque()
  for pos, prior in enumerate(prior_li):
    if pos == target_doc_loc:
      q.append((pos, prior, True))
    else :
      q.append((pos, prior, False))
  
  print(find_doc_count(q))