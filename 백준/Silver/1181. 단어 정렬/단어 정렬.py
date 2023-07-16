import sys
input = sys.stdin.readline

N = int(input())
word = []
for _ in range(N):
    temp = input().strip()
    word.append(temp)


word = list(set(word))
word.sort()
word.sort( key = len )
print("\n".join(word))