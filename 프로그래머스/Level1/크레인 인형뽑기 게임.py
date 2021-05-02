# https://programmers.co.kr/learn/courses/30/lessons/64061
def solution(board, moves):
    answer = 0
    n = len(board)
    tmp = []
    for move in moves:
        move = move - 1
        for i in range(n):
            if board[i][move]:

                tmp.append(board[i][move])
                board[i][move] = 0

                if len(tmp) > 1 and tmp[-1] == tmp[-2]:
                    tmp.pop()
                    tmp.pop()
                    answer += 2
                break

    return answer
