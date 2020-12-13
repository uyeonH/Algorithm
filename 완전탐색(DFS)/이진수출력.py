# 재귀함수

import sys

sys.stdin = open("in1.txt", "r")

def DFS(x):
    if x == 0:
        return
    else:
        DFS(x//2)
        print(x % 2,end=' ')


if __name__ == "__main__":
    a = ""
    n = int(input())
    DFS(n)
