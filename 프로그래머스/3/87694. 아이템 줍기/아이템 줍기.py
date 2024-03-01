from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 직사각형 중 어떤 직사각형의 변 위에 존재하는 지를 파악하는 함수
    def getRectangleList(point):
        point_x, point_y = point
        rec_list = []
        for rec_num, rec in enumerate(rectangle):
            x1, y1, x2, y2 = rec
            if ((x1 == point_x or x2 == point_x) and y1 <= point_y <= y2) or ((y1 == point_y or y2 == point_y) and x1 <= point_x <= x2):
                rec_list.append(rec_num)
        return rec_list
    
    # 어떠한 직사각형의 내부에 존재하는 지 파악하는 함수
    def isInRectangle(point):
        point_x, point_y = point
        for rec in rectangle:
            x1, y1, x2, y2 = rec
            if x1 < point_x < x2 and y1 < point_y < y2:
                return True
        return False
    
    def checkSameRectangle(before, after):
        for bef in before:
            for aft in after:
                if bef == aft:
                    return True
        return False
    
    def bfs(start, end):
        queue = deque()
        queue.append((start, 0))
        visited = set()
        visited.add(start)

        vectors = [(0,0.5), (0,-0.5), (0.5, 0), (-0.5,0)]

        while queue:
            now_point, count = queue.popleft()
            print(now_point)
            if now_point == end:
                return count
            
            hubos = []
            # 현재 위치에서 상,하,좌,우로 이동할 수 있는 지 체크한다.
            before = getRectangleList(now_point)
            for vec in vectors:
                check_point = (now_point[0] + vec[0], now_point[1] + vec[1])
                # 움직인 지점이 직사각형들의 변에 해당되는지를 확인한다.
                after = getRectangleList(check_point)
                # 동일한 사각형에서 이동한 것인지 확인한다. -> 폭이 1개짜리인거 점프하는거 체크 못함
                if checkSameRectangle(before, after):
                    if not isInRectangle(check_point):
                        check_point = (now_point[0] + vec[0], now_point[1] + vec[1])
                        # 변에 해당된다면, visited에 해당되는지 않는지도 확인한다.
                        if check_point not in visited:
                            visited.add(check_point)
                            queue.append((check_point, count+1))

    answer = bfs((characterX, characterY), (itemX, itemY))
    return answer // 2