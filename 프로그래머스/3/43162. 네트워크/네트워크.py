from collections import deque
def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def bfs(start):
        queue = deque([start])
        visited[start] = True
        
        while queue:
            cur_com = queue.popleft()
            
            for index, adaj_com in enumerate(computers[cur_com]):
                if adaj_com == 1 and not visited[index]:
                    queue.append(index)
                    visited[index] = True
                    
    for com in range(n):
        if visited[com] == False:
            bfs(com)
            answer += 1
        
    return answer


    