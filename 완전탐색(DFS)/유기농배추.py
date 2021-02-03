import sys
sys.setrecursionlimit(50000)
def dfs(x, y):
    visited[x][y] = 1

    global nums

    if matrix[x][y] == 1:
        nums += 1

    for p in range(4):

        nx = x + dx[p]
        ny = y + dy[p]

        if M > nx >= 0 and N > ny >= 0:

            if matrix[nx][ny] == 1 and visited[nx][ny] == 0:
                dfs(nx, ny)


if __name__ == '__main__':
    T = int(input())
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    res = []
    nums = 0

    for _ in range(T):
        worms = []
        nums = 0
        M, N, K = map(int, input().split())

        visited = [[0] * N for _ in range(M)]
        matrix = [[0] * N for _ in range(M)]

        for i in range(K):
            x, y = map(int, input().split())
            matrix[x][y] = 1

        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 1 and visited[i][j] == 0:
                    dfs(i, j)
                    worms.append(nums)
                    nums = 0

        res.append(len(worms))

    for i in res:
        print(i)
