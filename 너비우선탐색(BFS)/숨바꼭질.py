# 백준 1697 숨바꼭질 / BFS 1차원
# https://www.acmicpc.net/problem/2206

import sys
from collections import deque


def bfs(n):
    queue = deque()
    queue.append(n)
    visited[n] = 1
    while queue:
        x = queue.popleft()
        #print("현재 위치:", x)
        #print(queue)

        if x == k:
            print(visited[x]-1)
            break
        for pos in (x + 1, x - 1, 2 * x):
            if 0 <= pos < LIMIT and visited[pos] == 0:
                visited[pos] = visited[x] + 1
                queue.append(pos)


if __name__ == '__main__':
    LIMIT = 100001
    n, k = map(int, sys.stdin.readline().split())
    visited = [0] * LIMIT
    bfs(n)
