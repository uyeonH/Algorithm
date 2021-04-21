# 퇴사 DP
import sys

n = int(input())
Time, Pay = [0] * (n + 1), [0] * (n + 1)

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    Time[i] = a
    Time[i] = b

dp = [0] * (n + 1)

for i in range(len(Time) - 2, -1, -1): # n, n-1, ... , 0
    if Time[i] + i <= n: # n일 이내에 끝나면
        dp[i] = max(Pay[i] + dp[i + Time[i]], dp[i + 1])
    else: 
        dp[i] = dp[i + 1]

print(dp[0])
