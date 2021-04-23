import pprint
import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline
'''

1. dir에 다양한 조합의 방향을 넣는다

2. cctv 번호를 확인하고 이동한다.

3. 카메라 5는 네 방향 모두 감시할 수 있으므로 가장 먼저 처리해준다.

dfs 하단에 중복조합 느낌나는 for문은 연구소 문제에서도 비슷햇다.

(이해하기 위해 프린트문 남발,,

'''

def dfs(cnt):
    global ans, tmp

    if cnt == len(cctv):
        #print("cctv:", cctv)

        tmp = deepcopy(a)
        c = 0
        for i in range(len(cctv)):
            #print(i,dir[i])
            x, y = cctv[i]
            #print("cctv 위치 차례로 검사중(",x,",", y,")")
            if a[x][y] == 1:
                #print("카메라 1")
                c += move(x, y, dir[i])

            elif a[x][y] == 2:
                #print("카메라 2")
                c += move(x, y, dir[i])
                c += move(x, y, (dir[i] + 2) % 4)

            elif a[x][y] == 3:
                #print("카메라 3")
                c += move(x, y, dir[i])
                c += move(x, y, (dir[i] + 1) % 4)

            else:
                #print("카메라 4")
                c += move(x, y, dir[i])
                c += move(x, y, (dir[i] + 1) % 4)
                c += move(x, y, (dir[i] + 2) % 4)

        ans = min(ans, area - c)
        return

    for i in range(4):
        dir.append(i)
        #print("dir:",dir)
        dfs(cnt + 1)
        dir.pop()


def move(x, y, d):
    #print(" ## move ## ")
    #print("start:", x, ",", y)
    #print("dir:", d)
    cnt = 0
    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        #print("nx, ny, cnt", nx, ny, cnt)
        if not 0 <= nx < n or not 0 <= ny < m or tmp[nx][ny] == 6:
            return cnt
        if 0 < tmp[nx][ny] < 6 or tmp[nx][ny] == -1:
            x, y = nx, ny
            continue
        tmp[nx][ny] = -1
        cnt += 1
        x, y = nx, ny


def type5():
    global area
    for i in range(len(cctv5)):
        x, y = cctv5[i]
        for i in range(4):
            nx, ny = x, y
            while True:
                nx += dx[i]
                ny += dy[i]
                if not 0 <= nx < n or not 0 <= ny < m or a[nx][ny] == 6:
                    break
                if 0 < a[nx][ny] < 6 or a[nx][ny] == -1:
                    continue
                a[nx][ny] = -1
                area -= 1


if __name__ == '__main__':
    n, m = map(int, input().split())
    area = n * m
    a, cctv, cctv5 = [], [], []
    dx, dy = (1, 0, -1, 0), (0, -1, 0, 1)

    for i in range(n):
        row = list(map(int, input().split()))
        a.append(row)
        for j in range(m):
            if 0 < a[i][j] < 5:
                cctv.append([i, j])
                area -= 1
            elif a[i][j] == 5:
                cctv5.append([i, j])
                area -= 1
            elif a[i][j] == 6:
                area -= 1
    type5()
    p = pprint.PrettyPrinter(indent=5, width=40)

    dir = deque()
    ans = area
    dfs(0)
    print(ans)
