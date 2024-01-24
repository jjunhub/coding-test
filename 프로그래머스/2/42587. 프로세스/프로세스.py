from collections import deque 
def solution(priorities, location):
    processes = deque()
    answer = 0
    for pri in priorities:
        processes.append(pri)
        
    while processes:
        
        if max(processes) == processes[0]:
            processes.popleft()
            answer += 1
            if location == 0:
                return answer
        else :
            processes.rotate(-1)
            
        location = location - 1 if location > 0 else len(processes) - 1
        
    return answer