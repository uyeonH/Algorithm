from collections import deque

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer, q = 0, deque()


def get(i, j):
    if board[i][j]:
        q.append(board[i][j])  # 보드에서 0이 아닌 수를 큐에 저장
        board[i][j] = 0


def merge(i, j, di, dj):
    while q:
        x = q.popleft()

        if not board[i][j]:  # 0이면 그대로
            board[i][j] = x

        elif board[i][j] == x:  # 같으면 2배
            board[i][j] = x * 2
            i, j = i + di, j + dj

        else:  # 다르면
            i, j = i + di, j + dj
            board[i][j] = x


def move(k):
    if k == 0:  # 위
        for j in range(n):
            for i in range(n):
                get(i, j)
            merge(0, j, 1, 0)
    elif k == 1: # 아래
        for j in range(n):
            for i in range(n - 1, -1, -1):
                get(i, j)
            merge(n - 1, j, -1, 0)
    elif k == 2: # 오른쪽
        for i in range(n):
            for j in range(n):
                get(i, j)
            merge(i, 0, 0, 1)
    else: # 왼쪽
        for i in range(n):
            for j in range(n - 1, -1, -1):
                get(i, j)
            merge(i, n - 1, 0, -1)


def solve(count):
    global board, answer

    if count == 5:
        for i in range(n):
            answer = max(answer, max(board[i]))
        return

    b = [x[:] for x in board] # 그대로 저장

    for k in range(4):
        move(k)
        solve(count+1)
        board=[x[:] for x in b]


solve(0)
print(answer)
