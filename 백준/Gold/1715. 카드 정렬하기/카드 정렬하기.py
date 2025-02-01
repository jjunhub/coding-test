import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
cards = list()
answer = 0

for _ in range(N):
  heappush(cards, int(input()))

while len(cards)>1:
  card_one = heappop(cards)
  card_two = heappop(cards)
  answer += card_one + card_two
  heappush(cards, (card_one + card_two))

print(answer)