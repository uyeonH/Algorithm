import copy
import sys
from collections import deque

def bfs():
    global ans
    q = deque(virus)
    w = copy.deepcopy(board)
    cnt = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if w[nx][ny] == 0:
                    w[nx][ny] = 2
                    q.append([nx, ny])
    for i in w:
        cnt += i.count(0)
    ans = max(ans, cnt)


def wall(p, q, x):
    if x == 3:  # 벽 3개
        bfs()
        return
    for i in range(p, n):
        for j in range(q, m):
            if board[i][j] == 0:
                board[i][j] = 1
                wall(i, j, x + 1)
                board[i][j] = 0
        q = 0


n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)
ans = 0
virus = []
# 1:벽, 2:바이러스
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            virus.append([i, j])
wall(0, 0, 0)
print(ans)
