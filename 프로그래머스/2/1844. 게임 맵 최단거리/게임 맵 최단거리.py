from collections import deque
def solution(maps):
    answer = -1
    row = len(maps) # 세로
    col = len(maps[0]) # 가로
    
    queue = deque()
    queue.append((0,0,1))
    visited = [[False] * col for _ in range(row)]
    dir = [(0,1), (0, -1), (1,0), (-1, 0)]
    
    while queue:
        cur_v_row, cur_v_col, route_len = queue.popleft()
        
        if maps[cur_v_row][cur_v_col] == 0:
            break
        
        if cur_v_row == row -1 and cur_v_col == col -1 :
            answer = route_len
            break
        
        for dir_row, dir_col in dir:
            now_row = cur_v_row + dir_row
            now_col = cur_v_col + dir_col
            
            if 0 <= now_col < col and 0 <= now_row < row :
                if maps[now_row][now_col] == 1 and visited[now_row][now_col] == False :
                    queue.append((now_row, now_col, route_len + 1))
                    visited[now_row][now_col] = True
                
    return answer