import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Ai = list(map(int, input().split()))

_sum = [0]
temp = _sum[0]
remain = [0] * M

count = -1 # because of _sum[0]
remain[0] -= 1 # because of _sum[0]

for i in Ai :
    temp += i
    _sum.append(temp % M)

# check for same remain case
for tempSum in _sum :
    if tempSum == 0 :
        count += 1
    remain[tempSum] += 1

for index in range(M):
    # If two prefix-sum have same remain, it can be divided by M.
    temp = remain[index]
    count += int(temp * ( temp - 1 ) / 2)

print(count)