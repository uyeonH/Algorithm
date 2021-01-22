import sys

sys.stdin = open("in1.txt", "r")


def DFS(v):
    global cnt
    global path
    if v == n:
        cnt += 1
        print(path) #경로 출력
    else:
        for i in range(1, n + 1):
            if A[v][i] == 1 and ch[i] == 0:
                ch[i] = 1
                path.append(i)
                DFS(i)
                path.pop()
                ch[i] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    A = [[0] * (n + 1) for i in range(n + 1)]
    ch = [0] * (n + 1)
    for _ in range(m):
        a, b = map(int, input().split())
        A[a][b] = 1
    # pprint.pprint(A)
    cnt = 0
    ch[1] = 1
    path=[]
    path.append(1)
    DFS(1)
    print(cnt)
