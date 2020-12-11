'''

게임에서 최후의 1인을 뽑아야한다. 
1명의 진행자가 있고 N명의 플레이어가 있다. 
플레이어는 동그랗게 둘러앉아 1번부터 N번까지 시계방향으로 돌아가며 번호를 외친다. 
진행자가 3을 외치면 3번 플레이어는 제외되고, 그 다음 플레이어부터 다시 1번부터 번호를 붙여 시작한다.
3번 플레이어가 되면 계속해서 원 밖으로 나오게된다.
이렇게 마지막까지 남은 1명이 최후의 1인이 된다.

'''
# 큐를 활용하여 문제를 해결했다. 
from collections import deque
import sys

# sys.stdin = open("in2.txt", "r")
a, b = map(int, input().split())
q = deque()
for i in range(a):
    q.append(i)

while len(q) != 1:
    for i in range(b - 1):
        q.append(q.popleft())
    q.popleft()
    # print(q)
print(q[0] + 1)
