from heapq import heapify, heappop, heappush
def solution(scoville, K):
    answer = 0
    
    heapify(scoville)
    while scoville[0] < K :
        if len(scoville) < 2 :
            return -1
        one = heappop(scoville)
        two = heappop(scoville) * 2
        heappush(scoville, one + two)
        answer += 1
        
        
    return answer