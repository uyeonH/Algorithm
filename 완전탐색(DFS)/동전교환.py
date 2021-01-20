import sys

sys.stdin = open("in1.txt", "r")


def DFS(L,sum_):# L은 사용한 동전의 갯수
    global res
    if sum_ >target:
        return
    if sum_ == target:
        if L <res:
            res=L
    else:
        for i in range(n):
             DFS(L+1,sum_+type[i])

if __name__ == "__main__":
    n = int(input())
    type = list(map(int, input().split()))
    type.sort(reverse=True)
    target = int(input())
    res=2147000000
    DFS(0,0)
    print(res)
