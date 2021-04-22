# 스타트와 링크
# https://www.acmicpc.net/problem/14889

'''
두 팀으로 나누어 능력치 차이가 최소가 되게 하는 문제
dfs

'''
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = int(1e9)
visited = [0] * n


def dfs(idx, cnt):
    print(idx,cnt)
    global ans
    if cnt == n // 2: # 절반이 같은 팀으로 갔을 때
        start, link = 0, 0
        # 능력치 계산
        for i in range(n):
            for j in range(n):
                # 둘다 같은 팀: start 팀
                if visited[i] and visited[j]:
                    start += arr[i][j]
                # 둘이 다른 팀: link 팀    
                elif not visited[i] and not visited[j]:
                    link += arr[i][j]
        ans = min(ans, abs(start - link))
        
    # 차례로 방문
    for i in range(idx, n):
        if visited[i]:
            continue
        visited[i] = 1
        dfs(idx + 1, cnt + 1)
        visited[i] = 0


dfs(0, 0)
print(ans)
