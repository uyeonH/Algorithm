# 백준 3190 뱀 문제
# 1: 사과, 2: 뱀 몸체
from collections import deque
from pprint import PrettyPrinter

p = PrettyPrinter(indent=4, width=40)


def rotate(d, dir_ch):
    if dir_ch == 'L':  # 왼
        d = (d - 1) % 4
    else:  # 오
        d = (d + 1) % 4
    return d


# 상, 우, 하, 좌 (시계방향)
dy, dx = (-1, 0, 1, 0), (0, 1, 0, -1)


def start():
    #p.pprint(board)
    time = 1
    dir = 1  # 처음 시작, 오른쪽
    y, x = 0, 0
    visited = deque([[y, x]])
    while True:
        y, x = y + dy[dir], x + dx[dir]
        if 0 <= y < n and 0 <= x < n and board[y][x] != 2:
            if not board[y][x]:  # 0이면, (사과x)
                tmp_y, tmp_x = visited.popleft()
                board[tmp_y][tmp_x] = 0  # 꼬리 제거
            board[y][x] = 2
            visited.append([y, x])
            if time in times.keys():
                dir = rotate(dir, times[time])
            time += 1
        else:
            return time


if __name__ == '__main__':
    n = int(input())
    board = [[0] * n for _ in range(n)]
    apple_count = int(input())

    for a in range(apple_count):
        y, x = map(int, input().split())
        board[y-1][x-1] = 1  # 사과

    move_count = int(input())
    times = {}

    for m in range(move_count):
        t, dir = input().split()
        times[int(t)] = dir

    print(start())
