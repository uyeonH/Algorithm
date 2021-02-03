# https://www.acmicpc.net/problem/2667
# 백준 - 단지 번호 붙이기

def dfs(x, y):
    global nums
    visited_list[x][y] = 1
    if matrix[x][y] == 1:
        nums += 1
    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            if matrix[nx][ny] == 1 and visited_list[nx][ny] == 0:
                dfs(nx, ny)


if __name__ == '__main__':
    n = int(input())
    matrix = []
    visited_list = [[0] * n for _ in range(n)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    nums = 0
    num_list = []
    for _ in range(n):
        matrix.append(list(map(int, list(input()))))

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1 and visited_list[i][j] == 0:
                dfs(i, j)
                num_list.append(nums)
                nums = 0

print(len(num_list))
for i in sorted(num_list):
    print(i)
