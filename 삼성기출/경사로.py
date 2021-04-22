# 경사로
# https://www.acmicpc.net/problem/14890
'''

1. 내려가는지 올라가는지 구분이 필요
2. 경사로가 겹치지 않기 위해 sw 리스트에 체크
3. 특정 위치 기준 특정 길이만큼 평평한지 확인 - 앞, 뒤로

'''
def dfs(road):
    global answer
    sw = [False] * n
    for i in range(n - 1):
        if road[i] == road[i + 1]:
            continue
        if abs(road[i] - road[i + 1]) > 1:
            return False

        if road[i] > road[i + 1]:  # 내려갈때
            tmp = road[i+1]
            for j in range(i+1, i +1+ L):
                if 0 <= j < n:
                    if road[j] != tmp:
                        return False
                    if sw[j] == True:
                        return False
                else:
                    return False
            sw[j] = True

        elif road[i] < road[i + 1]:  # 올라갈때
            tmp = road[i]
            for j in range(i, i - L, -1):
                if 0 <= j < n:
                    if road[j] != tmp:
                        return False
                    if sw[j] == True:
                        return False
                else:
                    return False

            sw[j] = True
    return True


if __name__ == '__main__':
    n, L = map(int, input().split())
    answer = 0
    arr = [list(map(int, input().split())) for _ in range(n)]
    for a in arr:
        if dfs(a):
            #print(a)
            answer += 1
    for i in range(n):
        a = []
        for j in range(n):
            a.append(arr[j][i])
        if dfs(a):
            #print(a)
            answer += 1
    print(answer)
