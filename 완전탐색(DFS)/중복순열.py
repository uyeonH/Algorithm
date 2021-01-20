import sys

sys.stdin = open("in2.txt", "r")


def DFS(L):
    global cnt
    if L == m:
        cnt+=1
        for i in res:
            print(i, end=' ')
        print()

    else:
        for i in range(1,n+1):
            res[L]=i
            DFS(L+1)


if __name__ == "__main__":
    n, m = map(int, input().split())  # 1~n 중 m개
    res = [0] * m
    cnt = 0
    DFS(0)
    print(cnt)
