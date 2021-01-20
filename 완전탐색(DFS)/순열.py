'''
input
3 2

output
1 2
1 3
2 1
2 3
3 1
3 2
6

'''

import sys
#sys.stdin = open("in2.txt", "r")

def DFS(L):
    global cnt
    global ch
    if L == m:
        cnt += 1
        for i in res:
            print(i, end=' ')
        print()

    else:
        for i in range(1, n + 1):
            if ch[i-1] == 0:
                res[L] = i
                ch[i-1]=1
                DFS(L + 1)
                ch[i-1] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())  # 1~n 중 m개
    res = [0] * m
    ch = [0] * n
    cnt = 0
    DFS(0)
    print(cnt)
