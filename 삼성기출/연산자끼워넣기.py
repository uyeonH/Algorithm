# 연산자 끼워넣기
# https://www.acmicpc.net/problem/14888


n = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = list(map(int, input().split()))
count = add + sub + mul + div
answer_max = -100000000
answer_min = 100000000


def dfs(L, add, sub, mul, div, mid_sum):
    global answer_max, answer_min
    print(L, add, sub, mul, div, mid_sum)
    if L == count:
        answer_max = max(answer_max, mid_sum)
        answer_min = min(answer_min, mid_sum)
        return

    if add:
        dfs(L + 1, add - 1, sub, mul, div, mid_sum + numbers[L + 1])

    if sub:
        dfs(L + 1, add, sub - 1, mul, div, mid_sum - numbers[L + 1])

    if mul:
        dfs(L + 1, add, sub, mul - 1, div, mid_sum * numbers[L + 1])

    if div:
        if mid_sum < 0:
            x = -int(-mid_sum / numbers[L + 1])
        else:
            x = int(mid_sum / numbers[L+1])
        dfs(L + 1, add, sub, mul, div - 1, x)


dfs(0, add, sub, mul, div, numbers[0])

print(answer_max)
print(answer_min)
