N = int(input())
place = list(map(int, input().split()))
B, C = map(int, input().split())
cnt = 0

# 총 감독관 처리
for i in range(N):
    if place[i] > 0:
        place[i] = place[i] - B
        cnt += 1

# 부감독관 처리

for i in range(N):
    if place[i] > 0:

        cnt = cnt + place[i] // C
        if place[i] % C !=0:
            cnt+=1




print(cnt)
