import copy
from collections import deque



def dfs():
    global result
    q = deque(virus)
    board2 = copy.deepcopy(board)
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if board2[nx][ny] == 0:
                board2[nx][ny] = 2
                q.append([nx, ny])
    for b in board2:
        cnt += b.count(0)
    result = max(result, cnt)


def wall(p, q, depth):
    if depth == 3:
        dfs()
        return
    else:
        for i in range(p, n):
            for j in range(q, m):
                print(i,j)
                if board[i][j] == 0:
                    board[i][j] = 1
                    wall(i, j, depth + 1)
                    board[i][j] = 0
            q = 0

if __name__ == '__main__':
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    # 1: 벽, 2: 바이러스
    virus = []
    result = 0
    dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                virus.append([i, j])
    wall(0, 0, 0)
    print(result)
