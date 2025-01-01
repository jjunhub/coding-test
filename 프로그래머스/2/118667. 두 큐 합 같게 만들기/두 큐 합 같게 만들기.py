from collections import deque

# 두 큐의 합을 각각 구해서, 합이 더 큰 곳에서 pop해서 작은 곳으로 Push합니다.
def solution(queue1, queue2):
    dq1, dq1_sum = deque(queue1), sum(queue1)
    dq2, dq2_sum = deque(queue2), sum(queue2)
    total_len = len(queue1) + len(queue2)
    
    tick = 0
    while dq1_sum != dq2_sum and tick != 2 * total_len: 
        if dq1_sum > dq2_sum:
            element = dq1.popleft()
            dq2.append(element)
        
            dq1_sum -= element
            dq2_sum += element    
        else:
            element = dq2.popleft()
            dq1.append(element)
        
            dq1_sum += element
            dq2_sum -= element
        tick += 1
    
    if tick == 2 * total_len:
        answer = -1
    else :
        answer = tick
    return answer