'''
input
3
1 2 5
15

output
3

'''

import sys

sys.stdin = open("in5.txt", "r")

import time


def DFS(L, sum_):  # L은 사용한 동전의 갯수
    global res
    if sum_ > target: # 현재 위치에서 합이 목표보다 크면 종료
        return
    if L > res: # 이미 나온 결과값보다 값이 크면 종료
        return
    if sum_ == target:
        if L < res:
            res = L
    else:
        for i in range(n):
            DFS(L + 1, sum_ + type[i])


if __name__ == "__main__":
    start_time = time.time()
    n = int(input())
    type = list(map(int, input().split()))
    type.sort(reverse=True)
    target = int(input())
    res = 2147000000
    DFS(0, 0)
    print(res)
    end_time = time.time()
    #print("실행 시간: ", end_time - start_time)
