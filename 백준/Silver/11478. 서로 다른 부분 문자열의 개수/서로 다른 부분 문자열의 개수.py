import sys
input = sys.stdin.readline

S = input().rstrip()
words = {}

for length in range(1, len(S)+1):
  for i in range(0, len(S)-length+1):
    word = S[i:i+length]
    if word not in words:
      words[word] = 1

print(len(words))