def solution(places):
    for place in places:
        arr = [] # 5*5 배열
        pos = [] # P들 좌표 저장
        # 문자열 배열로 바꾸기, P 좌표 구하기
        for i in range(len(place)):
            row = place[i]
            arr.append(list(row))
            for j in range(len(row)):
                val = row[j]
                if val == 'P':
                    pos.append((i, j))

        answer.append(bfs(pos, arr))
        
    return answer


def bfs(pos, arr):
    for x, y in pos:
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if 0 <= nx < 5 and 0 <= ny < 5:
                
                # 상하좌우에 바로 P가 있으면
                if arr[nx][ny] == 'P':
                    return 0
                
                # 빈 테이블이 있으면 검사
                elif arr[nx][ny] == 'O':
                    
                    # 테이블이 위나 아래에 있을 때
                    if dx[k] == 0:                          
                        
                        # 좌
                        ax = nx + dx[2]
                        ay = ny + dy[2]                      
                                            
                        if 0 <= ax < 5 and 0 <= ay < 5:
                            if arr[ax][ay] == 'P':
                                return 0
                        # 우
                        bx = nx + dx[3]
                        by = ny + dy[3]
                        
                        if 0 <= bx < 5 and 0 <= by < 5:
                            if arr[bx][by] == 'P':
                                return 0

                        # 같은 방향                        
                        cy = ny + dy[k]
                        if 0 <= cy < 5:
                            if arr[nx][cy] == 'P':
                                return 0
                        
                    # 테이블이 좌우에 있을 때
                    elif dy[k] == 0:   
                        
                        # 상
                        ax = nx + dx[0]
                        ay = ny + dy[0]
                        
                        if 0 <= ax < 5 and 0 <= ay < 5:
                            if arr[ax][ay] == 'P':
                                return 0
                        
                        # 하                        
                        bx = nx + dx[1]
                        by = ny + dy[1]                                                
                            
                        if 0 <= bx < 5 and 0 <= by < 5:
                            if arr[bx][by] == 'P':
                                return 0
                        
                        # 같은 방향                        
                        cx = nx + dx[k]
                        if 0 <= cx < 5:
                            if arr[cx][ny] == 'P':
                                return 0

    return 1


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
answer = []
