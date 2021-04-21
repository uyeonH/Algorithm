import sys

input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def clean(x, y, d):
    global ans
    if arr[x][y] == 0:
        arr[x][y] = 2
        ans += 1
    for _ in range(4):
        nd = (d + 3) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        if arr[nx][ny] == 0:
            clean(nx, ny, nd)
            return
        d = nd
    nd = (d + 2) % 4 # 뒤 방향
    nx = x + dx[nd]
    ny = y + dy[nd]
    if arr[nx][ny] == 1:
        return
    clean(nx, ny, d) # 후진이므로 방향은 d

if __name__ == '__main__':

    n, m = map(int, input().split())
    x, y, d = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    clean(x, y, d)
    print(ans)
