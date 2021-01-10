import sys

sys.stdin = open("in5.txt", "r")

# L: index of list_
# tsum: 현재 가지까지 판단한 무게의 합, sum_에 포함되지 않았더라도,
# 그렇다면 total-tsum은? 앞으로 판단해야 할 바둑이의 무게

def DFS(L, sum_, tsum):
    global max_
    
    # 지금까지 더한 값에 앞으로 더하게 될 모든 수를 더했는데도 
    # 최대값보다 작다면 더이상 계산할 필요가 없다. 
    if sum_+(total-tsum)<max_:
        return

    # 상한선 체크
    if sum_ > c:
        return

    if L == n:
        
        if sum_ > max_:
            max_ = sum_

    else:
        DFS(L + 1, sum_, tsum + list_[L])
        DFS(L + 1, sum_ + list_[L], tsum + list_[L])


if __name__ == "__main__":
    c, n = map(int, input().split())
    list_ = []
    
    for _ in range(n):
        list_.append(int(input()))
        
    max_ = 0
    total=sum(list_)
    
    DFS(0, 0, 0)
    
    print(max_)
