'''
# 응급실

응급실은 환자가 도착한 순서대로 진료를 한다. 하지만 위험도가 높은 환자는 빨리 응급조치를 해야한다. 
이런 문제를 보완하기 위해 응급실은 다음과 같은 방법으로 환자의 진료순서를 정한다.

• 환자가 접수한 순서대로의 목록에서 제일 앞에 있는 환자목록을 꺼낸다
• 나머지 대기 목록에서 꺼낸 환자 보다 위험도가 높은 환자가 존재하면 대기목록 제일 뒤로 다시 넣는다.

현재 N명의 환자가 대기목록에 있다
N명의 대기목록 순서의 환자 위험도가 주어지면, 대기목록상의 M번째 환자는 몇 번째로 진료를 받는지 출력하는 프로그램을 작성하라.
대기목록상의 M번째는 대기목록의 제일 처음 환자를 0번째로 간주하여 표현한 것이다.

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
