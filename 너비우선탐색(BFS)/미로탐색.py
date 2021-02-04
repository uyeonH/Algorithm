
# 백준 2178번
# https://www.acmicpc.net/problem/status/2178
def bfs():

    queue = [(0, 0)]
    visited[0][0] = 1

    while queue:
        x, y = queue.pop(0)

        if x == tx and y == ty:
            print(visited[x][y])
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and matrix[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))


if __name__ == '__main__':

    n, m = map(int, input().split())
    matrix = []
    visited = [[0] * m for _ in range(n)]

    tx = n - 1
    ty = m - 1
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    res = []

    distance = 0

    for _ in range(n):
        matrix.append(list(map(int, list(input()))))

    bfs()
