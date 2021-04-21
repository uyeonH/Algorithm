# 퇴사
# https://www.acmicpc.net/problem/14501

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
# 일수, 페이

sum_p = 0


def dfs(L, sum):
    global sum_p
    if L>n:
        return
    if L == n:
        sum_p = max(sum_p, sum)
        return

    else:
        # 안하는 경우
        dfs(L + 1, sum)

        # 하는 경우
        dfs(L + s[L][0], sum + s[L][1])


dfs(0, 0)
print(sum_p)
