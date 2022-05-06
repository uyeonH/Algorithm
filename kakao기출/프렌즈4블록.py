def solution(m, n, board):
    answer = 0
    arr = [list(row) for row in board]

    def remove(arr, m, n):
        chk = [[False for _ in range(n)] for _ in range(m)]
        for r in range(m - 1):
            for c in range(n - 1):
                block = arr[r][c]
                if block == arr[r][c + 1] == arr[r + 1][c] == arr[r + 1][c + 1]:
                    chk[r][c] = True
                    chk[r][c + 1] = True
                    chk[r + 1][c] = True
                    chk[r + 1][c + 1] = True

        removed_blocks = 0
        for r in range(m):
            for c in range(n):
                if chk[r][c] and arr[r][c] != "":
                    arr[r][c] = ""
                    removed_blocks += 1
        return removed_blocks

    def drop(arr):
        # 블록이 떨어짐
        for c in range(n):
            cnt = 0
            for r in range(m - 1, -1, -1):
                if arr[r][c] == "":
                    cnt += 1
                elif cnt > 0:
                    arr[r + cnt][c] = arr[r][c]
                    arr[r][c]=""

    while True:
        blocks = remove(arr, m, n)
        if blocks == 0:
            return answer
        answer += blocks
        drop(arr)

    return blocks
