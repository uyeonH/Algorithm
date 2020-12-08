'''
# 회의실 정하기

한 개의 회의실을 사용하고자하는 n개의 회의들이 있다.
각 회의에 대해 시작 시간과 종료 시간이 주어진다. 
회의 시간이 겹치지 않게 회의실을 사용하는 최대수의 회의를 찾아라.
(끝나는 동시에 다른 회의 시작 가능, 도중에 멈출 수 x)

첫째 줄에 회의 수, 둘째 줄부터 회의 시작 시간, 끝나는 시간이 주어진다.

# input
5
1 4
2 3
3 5
4 6
5 7

# output
3

'''


import sys
sys.stdin = open("in2.txt", "r")
n = int(input())
meeting = []

for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e))

# 회의 끝나는 시간대로 정렬을 해준다. 끝나는 시간에 맞추어 다음 회의를 시작하면 된다. 
meeting.sort(key=lambda x: (x[1], x[0]))  # x[1]을 우선순위로 정렬 / 람다 함수 사용

cnt = 1
et = meeting[0][1]

for x, y in meeting:
    if x >= et:
        cnt += 1
        et = y
        
print(cnt)



# 출처: [인프런 파이썬 알고리즘 문제풀이 (코딩테스트) 대비 강의]
# Link: https://www.inflearn.com/course/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8/dashboard
