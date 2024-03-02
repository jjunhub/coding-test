from collections import deque 
def solution(n, edge):
    answer = 0
    visited = [False] * (n+1)
    graph = [ [] for _ in range(n+1)] # index 0 is dummy
    distance = [0] * (n+1)
        
    for start, end in edge:
        graph[start].append(end)
        graph[end].append(start)

    def bfs(start):
        queue = deque()
        queue.append((start,0))
        visited[start] = True
        
        while queue:
            cur_node, count = queue.popleft()
            distance[cur_node] = count
            for next_node in graph[cur_node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    queue.append((next_node,count+1))
    
    bfs(1)
    answer = distance.count(max(distance))
    return answer