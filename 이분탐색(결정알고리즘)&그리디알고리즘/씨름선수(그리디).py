'''
# 씨름선수

N명의 씨름 선수가 시합에 지원했다. 이들의 키와 몸무게를 알고있다.
선수의 선발 조건은 다음과 같다.
" 다른 모든 지원자와 일대인 비교하여 키와 몸무게 중 적어도 하나는 크거나 무거운 지원자만 뽑는다."
만약 A 지원자보다 키도 크고 몸무게도 무거운 지원자가 존재하면 A는 탈락이다.

# input
5
172 67
183 65
180 70
170 72
181 60

# output
3


'''

import sys

sys.stdin = open("in2.txt", "r")
n = int(input())
player = []

for i in range(n):
    s, e = map(int, input().split())
    player.append((s, e))

player.sort(reverse=True) # 키 내림차순으로 정렬

w_max=player[0][1]
cnt=1

# 더이상 키는 생각하지 않아도 된다. 
# 몸무게는 앞에 키가 큰 선수들의 몸무게보다 커야한다. 즉, 앞의 선수들의 키의 max값보다 크면 카운팅한다.

for h,w in player:
    if w>w_max:
        cnt+=1
        w_max=w
        
print(cnt)

