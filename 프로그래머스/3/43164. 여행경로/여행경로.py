from collections import defaultdict
def solution(tickets):
    answer = ["ICN"]
    routes = defaultdict(list)
    answerList = []
    
    for ticket in tickets:
        start, end = ticket
        routes[start].append(end)
    
    for key in routes:
        routes[key].sort(reverse=True)        
        
    visited = []
    
    def dfs(start):
        while routes[start]:
            next = routes[start].pop()
            dfs(next)
        visited.append(start)
    
    dfs("ICN")
    visited.reverse()
    
    return visited
    