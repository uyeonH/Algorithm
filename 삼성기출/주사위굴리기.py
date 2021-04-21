# 주사위 굴리기
# https://www.acmicpc.net/problem/14499

N, M, x, y, K = map(int, input().split())
board = [[0] * M for _ in range(N)]

for i in range(N):
    board[i] = list(map(int, input().split()))

commands = map(int, input().split())

dx, dy = (0, 0, -1, 1), (1, -1, 0, 0)  # 동, 서, 북, 남

dice = [0] * 6  # 왼쪽 옆면, 윗면, 오른쪽 옆면, 뒷면, 앞면, 바닥 // 맨 처음


def change_direct(dir):
    #print("방향",dir)
    global dice
    ndice = [0] * 6

    if dir == 1:  # 동
        ndice[0] = dice[5]
        ndice[1] = dice[0]
        ndice[2] = dice[1]
        ndice[3] = dice[3]
        ndice[4] = dice[4]
        ndice[5] = dice[2]

    elif dir == 2:  # 서
        ndice[0] = dice[1]
        ndice[1] = dice[2]
        ndice[2] = dice[5]
        ndice[3] = dice[3]
        ndice[4] = dice[4]
        ndice[5] = dice[0]

    elif dir == 3:  # 북
        ndice[0] = dice[0]
        ndice[1] = dice[4]
        ndice[2] = dice[2]
        ndice[3] = dice[1]
        ndice[4] = dice[5]
        ndice[5] = dice[3]

    elif dir == 4:  # 남
        ndice[0] = dice[0]
        ndice[1] = dice[3]
        ndice[2] = dice[2]
        ndice[3] = dice[5]
        ndice[4] = dice[1]
        ndice[5] = dice[4]

    dice = ndice


def start(x, y):

    for c in commands:

        if 0 > x + dx[c - 1] or x + dx[c - 1] >= N or 0 > y + dy[c - 1] or y + dy[c - 1]>= M:
            continue
        else:
            change_direct(c)
            nx = x + dx[c - 1]
            ny = y + dy[c - 1]
            if board[nx][ny] == 0:  # 지도가 0일 때
                board[nx][ny] = dice[5]

            else:  # 칸이 0이 아니면
                dice[5] = board[nx][ny]
                board[nx][ny] = 0

            x = nx
            y = ny
            print(dice[1])


start(x, y)
