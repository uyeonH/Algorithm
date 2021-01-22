'''
# input
5 3
2 4 5 8 12
6

#output
2

'''
import sys
#sys.stdin = open("in2.txt", "r")

def DFS(L, s, sum_):
    global cnt
    if L <= m:

        if L == m and sum_ % k == 0:
            cnt += 1
        else:
            for i in range(s, n):
                DFS(L + 1, i + 1, sum_ + a[i])


if __name__ == "__main__":
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    k = int(input())
    cnt = 0
    DFS(0, 0, 0)
    print(cnt)
