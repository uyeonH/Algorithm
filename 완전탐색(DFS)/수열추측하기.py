import sys

sys.stdin = open("in1.txt", "r")


def DFS(L, sum_):
    global ch
    global p
    if L == n and sum_ == f:
        for x in p:
            print(x, end=' ')
        sys.exit(0)

    else:
        for i in range(1, n + 1):
            if ch[i] == 0:
                ch[i] = 1
                p[L] = i
                DFS(L + 1, sum_ + p[L]*b[L])
                ch[i] = 0


if __name__ == "__main__":

    n, f = map(int, input().split())

    p = [0] * n # 최상단 배열 저장용

    b = [1] * n # 파스칼 계수
    ch = [0] * (n + 1)

    #파스칼 계수 계산
    for i in range(1, n):
        b[i] = b[i - 1] * (n - i) // i

    DFS(0, 0)
