
'''

유람선에 N명의 승객이 타고있다. 구명보트를 타고 탈출해야하는데 구명보트는 2명 이하로만 탈 수 있다.
보트 한 개에 탈 수 있는 총 무게는 M kg 이하로 제한된다.
N명의 승객 몸무게가 주어졌을 때 승객 모두가 탈출하기 위한 구명보트의 최소 개수를 출력하라.

첫째 줄에 승객 수, 보트 제한 몸무게
둘째 줄에 승객의 몸무게
#input
5 140
90 50 70 100 60

#output
3

'''

import sys
from collections import deque
sys.stdin = open("in1.txt", "r")

n,w = map(int,input().split())
people = list(map(int,input().split()))
people.sort()
people=deque(people) # 자료구조상 효율성 높임
cnt=0

while people:
    if len(people)==1:
        cnt+=1
        break
    if people[0]+people[- 1]<=w:
        people.popleft() # 왼쪽 삭제 (꺼내기)
        people.pop() #오른쪽 삭제 (꺼내기)
        cnt+=1
    else:
        people.pop()
        cnt += 1

print(cnt)

