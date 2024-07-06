from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list) # ( w, n )
        visited = [0] * (n+1)
        visitedNode = set()
        
        # Make Graph with weight
        for edge in times :
            startNode, endNode, weight = edge
            graph[startNode].append((weight, endNode))
            
        minHeap = []
        heapq.heappush(minHeap, (0, k))
        while minHeap:
            current_weight, current_node = heapq.heappop(minHeap)
            
            if current_node not in visitedNode:
                visitedNode.add(current_node)
                visited[current_node] = current_weight
                
                for weight, nodeNum in graph[current_node]:
                    weight = weight + current_weight
                    heapq.heappush(minHeap, (weight, nodeNum))
        
        if len(visitedNode) != n:
            return -1
        else :
            return max(visited)
        
                    
                
            