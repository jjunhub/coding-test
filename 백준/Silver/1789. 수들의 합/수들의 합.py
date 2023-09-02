S = int(input())
answer = 1
_sum = 0

while(_sum <= S):
    _sum += answer
    answer +=1 

print(answer-2)