from collections import deque
def solution(n, results):
    answer = 0
    graph = [[] for _ in range(n)]
    check = [ [0] * n for _ in range(n) ]
    for win, lose in results:
        graph[win-1].append(lose-1)
        
    def bfs(start):
        queue = deque()
        queue.append(start)
        visited = {start}
        
        while queue:
            cur_person = queue.popleft()
            for next_person in graph[cur_person]:
                if next_person not in visited:
                    visited.add(next_person)
                    queue.append(next_person)
        return visited
        
    for start in range(n):
        visited = bfs(start)
        for end in visited:
            check[end][start] = 1
            check[start][end] = 1
    
    for temp in check:
        if all(temp) == 1:
            answer += 1
    return answer