'''
#input
5 9
1 2 
1 3
1 4 
2 1 
2 3 
2 5 
3 4 
4 2 
4 5

#output
6

'''

import sys

#sys.stdin = open("in1.txt", "r")


def DFS(v):
    global cnt
    if v == n:
        cnt += 1
    else:
        for i in range(1, n + 1):
            if A[v][i] == 1 and ch[i] == 0:
                ch[i] = 1
                DFS(i)
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
    DFS(1)
    print(cnt)
