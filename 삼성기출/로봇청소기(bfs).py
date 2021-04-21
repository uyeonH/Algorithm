# 로봇 청소기
# https://www.acmicpc.net/problem/14503

from collections import deque


def clean(x, y, d):
    global answer
    q = deque()
    q.append((x, y, d))

    while q:
        x, y, d = q.popleft()

        if arr[x][y] == 0:
            answer += 1
            arr[x][y] = 2

        for k in range(4):
            d = (d + 3) % 4
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = 2
                    answer += 1
                    q.append((nx, ny, d))
                    break

            if k == 3:
                nx, ny = x - dx[d], y - dy[d]
                if 0 <= nx < n and 0 <= ny < m and arr[nx][ny]!=1:
                    q.append((nx,ny,d))


n, m = map(int, input().split())
x, y, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx, dy = (-1, 0, 1, 0), (0, 1, 0, -1)  # 북 동 남 서
answer = 0
clean(x, y, d)
print(answer)
