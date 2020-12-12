'''
# 응급실

응급실은 환자가 도착한 순서대로 진료를 한다. 하지만 위험도가 높은 환자는 빨리 응급조치를 해야한다. 
이런 문제를 보완하기 위해 응급실은 다음과 같은 방법으로 환자의 진료순서를 정한다.
.
.
(문제 공개x)

# input
5 2
60 50 70 80 90

# output
3

'''

import sys
from collections import deque

sys.stdin = open("in1.txt", "r")
n, m = map(int, input().split())

# 환자의 위험도 정보 앞에 인덱싱 하는 방법
Q = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
Q = deque(Q)
#print(Q)

cnt = 0 # 진료 횟수 카운트

while True:
    cur = Q.popleft()
    if any(cur[1] < x[1] for x in Q): # Q에서 하나씩 꺼내와 비교 / 현재 환자와 위험도
        Q.append(cur)
    else:
        cnt += 1
        if cur[0] == m: # m번째 환자 치료시 프로그램 끝
            break
print(cnt)

#  출처: https://www.inflearn.com/course/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8/dashboard
