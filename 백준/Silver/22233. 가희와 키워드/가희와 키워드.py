import sys
input = sys.stdin.readline

N, M = map(int, input().split())
_memo = {}
for _ in range(N):
    word = input().rstrip()
    _memo[word] = 1

for _ in range(M):
    post = input().rstrip()
    words = post.split(',')

    for word in words:
        if word in _memo :
            _memo[word] = 0
            del _memo[word]
    
    print(len(_memo.keys()))