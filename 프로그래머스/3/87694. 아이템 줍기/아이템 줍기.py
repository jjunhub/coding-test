from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    
    # 직사각형의 변 위에 존재하는 지를 파악하는 함수
    def isOnRectangle(point):
        point_x, point_y = point
        for rec in rectangle:
            x1, y1, x2, y2 = rec
            if (x1 == point_x or x2 == point_x) and y1 <= point_y <= y2:
                return True
            if (y1 == point_y or y2 == point_y) and x1 <= point_x <= x2:
                return True
        return False
    
    # 어떠한 직사각형의 내부에 존재하는 지 파악하는 함수
    def isInRectangle(point):
        point_x, point_y = point
        for rec in rectangle:
            x1, y1, x2, y2 = rec
            if x1 < point_x < x2 and y1 < point_y < y2:
                return True
        return False
    
    def bfs(start, end):
        queue = deque()
        queue.append((start, 0))
        visited = {start}
        
        vectors = [(0,0.5), (0,-0.5), (0.5, 0), (-0.5,0)]

        while queue:
            now_point, count = queue.popleft()
            
            # 도착지점이라면 움직인 횟수를 반환한다.
            if now_point == end:
                return count
            
            # 현재 위치에서 상,하,좌,우로 0.5씩 이동할 수 있는 지 체크한다.
            for vec in vectors:
                check_point = (now_point[0] + vec[0], now_point[1] + vec[1])
                
                # 움직인 지점이 직사각형들의 변에 해당되는지, 직사각형의 내부에 존재하는 지 확인한다.
                if isOnRectangle(check_point) and not isInRectangle(check_point):
                    
                    # 변에 해당된다면, visited에 해당되는지 않는지도 확인한다.
                    if check_point not in visited:
                        visited.add(check_point)
                        queue.append((check_point, count+0.5))

    answer = bfs((characterX, characterY), (itemX, itemY))
    return answer