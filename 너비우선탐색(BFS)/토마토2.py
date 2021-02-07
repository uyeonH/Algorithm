# 백준 7569번 토마토
# https://www.acmicpc.net/problem/7569

import pprint
from collections import deque


def bfs():
    global m
    days = -1
    while queue:
        #print(days)
        days += 1

        # matrix[z][x][y]=1
        for _ in range(len(queue)):
            z, x, y = queue.popleft()
            #print("현재 위치: ",z, x, y)
            #p.pprint(matrix)
            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[i]
                nz = z + dz[i]
                if (0 <= nx < n) and (0 <= ny < m) and (0 <= nz < h) and matrix[nz][nx][ny] == 0:
                    #print("이동할 위치: ",nz, nx, ny)
                    queue.append((nz, nx, ny))
                    matrix[nz][nx][ny] = matrix[z][x][y] + 1

    for i in range(h):
        for m in matrix[i]:
            #print(m)
            if 0 in m:
                return -1
    return days


if __name__ == '__main__':
    m, n, h = map(int, input().split())
    queue = deque()
    matrix = [[] for _ in range(h)]
    p = pprint.PrettyPrinter(indent=3, width=30)
    # print(matrix)
    dx = [1, 0, -1, 0, 0, 0]
    dy = [0, 1, 0, -1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]
    for k in range(h):
        for i in range(n):
            row = list(map(int, input().split()))
            for j in range(len(row)):
                if row[j] == 1:
                    queue.append((k, i, j))
            matrix[k].append(row)
    # print(matrix)
    print(bfs())
