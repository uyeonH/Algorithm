import sys
import pprint

pp = pprint.PrettyPrinter(indent=4)
sys.stdin = open("input.txt", 'r')
cnt = 0
board = [list(map(int, input().split())) for _ in range(7)]
# pp.pprint(board)


for i in range(3):  # 옆으로 이동하면서 5개씩 검사, 3번 돌면 된다.
    for j in range(7):  # 행 수, 아래쪽으로 검사
        b = board[j][i:i + 5]
        if b == b.reverse(): # 가로 검사, 뒤집은 것과 같다면
            #print(b)
            cnt += 1
        for k in range(2): # 세로 검사
            if board[i + k][j] != board[i + 5 - k - 1][j]: #가운데 수를 제외한 수를 비교
                break
            else:
                cnt += 1

print(cnt)
