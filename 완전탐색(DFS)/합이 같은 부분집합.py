
import sys

sys.stdin = open("in1.txt", "r")


def DFS(L, sum_):
    # L - index/level, sum_ - 부분 합
    print(L)
    if L == n:
        if total - sum_ == sum_: #  부분합과 리스트 총합 - 부분합이 같으면
            print("YES")
            sys.exit(0)
    else:
        DFS(L+1,sum_) # 현재 원소 포함x

        sum_ += a[L]
        DFS(L+1, sum_) # 현재 원소 포함

    
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    DFS(0, 0)
