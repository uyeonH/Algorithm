# 연구소
# https://www.acmicpc.net/problem/14502

'''
완전탐색 문제

1. 바이러스 위치를 찾는다
2. 벽을 3개 세운다
3. 바이러스를 퍼뜨려본다

주의: wall 함수쪽을 조합으로 해결하지 않으면 시간초과 발생

'''
import copy
from collections import deque

def dfs():
    global ans
    q = deque(virus)
    w = copy.deepcopy(board)
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if w[nx][ny] == 0:
                    w[nx][ny] = 2
                    q.append([nx, ny])
    for b in w:
        cnt += b.count(0)
    ans = max(ans, cnt)


def wall(p, q, depth):
    if depth == 3:
        dfs()
        return
    else:
        for i in range(p, n):
            for j in range(q, m):
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
    ans = 0
    dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                virus.append([i, j])
    wall(0, 0, 0)
    print(ans)
