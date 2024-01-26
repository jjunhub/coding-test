import collections
def solution(bridge_length, weight, truck_weights):
    answer = 0
    onBridgeW = 0
    q = collections.deque()
    truck_weights.reverse()
    
    while truck_weights:
        
        answer += 1
        if q and answer - q[-1][0] >= bridge_length: # Check last truck of q
            _, beforeWeight = q.pop()
            onBridgeW -= beforeWeight  
            
        if onBridgeW + truck_weights[-1] <= weight: # If weight is enough for add new truck...
            truck = truck_weights.pop()
            onBridgeW += truck
            q.appendleft((answer, truck))
            
    answer += bridge_length # Add time for remain truck at q
    return answer