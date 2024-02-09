from collections import deque
def solution(n, wires):
    # n은 노드(송전탑)의 개수, wires는 edge의 개수.
    # 모든 wires들을 각각 1번씩 짤라서 해봐야함.
    # 송전탑의 개수를 최대한 비슷하게.
    # 결과는 두 송전탑의 개수의 차이
    answer = n
    graph = { key : [ ] for key in range(1, n+1)}
    for start, end in wires:
        if end not in graph[start]:
            graph[start].append(end)
        if start not in graph[end]:
            graph[end].append(start)
            
    
    for start, end in wires:
        firstGraphVisited = bfs(1, graph, start, end)
        secondRoot = findNotVisitedTopNum(firstGraphVisited, n)
        secondGraphVisited = bfs(secondRoot, graph, start, end)
        
        firstTopNum = len(firstGraphVisited)
        secondTopNum = len(secondGraphVisited)
        absDiff = max(firstTopNum,secondTopNum) - min(firstTopNum, secondTopNum)
        
        if absDiff < answer:
            answer = absDiff
        
    return answer
    
def bfs(root, graph, start, end):
    visited = [root]
    q = deque([root])
    while q:
        cur_top = q.popleft()
        for top in graph[cur_top]:
            if start == cur_top and end == top:
                continue
            if end == cur_top and start == top:
                continue     
            if top not in visited:
                visited.append(top)
                q.append(top)
    return visited

def findNotVisitedTopNum(visited, n):
    for idx in range(1, n+1):
        if idx not in visited:
            return idx