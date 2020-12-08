'''
마구간 정하기(결정 알고리즘)
N개의 마구간이 수직선상에 있다. 각 마구간은 좌표를 가지고 있다. 
C 마리 말을 가지고 있는데 이 말들은 서로 가까이 있는 것을 싫어한다.
각 마구간에 한마리의 말만 넣을 수 있고, 가장 가까운 두 말의 거리가 최대가 되도록 배치하려고 한다.
C마리 말을 N개의 마구간에 배치했을 때, 가장 가까운 두 말의 거리가 최대가 되도록 하는 값은?
첫 줄에 N(3<=N<=200,000)과 C(2<=C<=N)이 주어진다.
둘째 줄부터 N개의 줄에 걸쳐 마구간 좌표가 한줄에 하나씩 주어진다.

# input
5 3
1
2
8
4
9

#output
3

'''


import sys

sys.stdin = open("input.txt", "r")

# 주어진 거리가 말을 배치하기에 적정한 값인지 확인하는 함수
def Count(distance):
    cnt = 1  # 말 마리수 (가장 첫번째 자리 무조건 배치)
    ep = List[0]  # end point
    for i in range(1, k):
        if List[i] - ep >= distance:  # 현재 배치할 자리 - end point
            cnt += 1
            ep=List[i]
    return cnt

k, n = map(int, input().split())
List = []
tmp = [0 for _ in range(k)]

for _ in range(k):
    List.append(int(input()))

List.sort()

# 가능한 최소 거리의 범위: lt ~ rt
lt = 1
rt = List[k - 1]
minn = rt
res = 1

# 이분탐색
while lt <= rt:
    mid = (lt + rt) // 2
    #print(mid)
    if Count(mid) >= n:
        minn = mid
        lt = mid + 1

    else:
        rt = mid - 1
    res = minn

print(res)



# 출처: [인프런 파이썬 알고리즘 문제풀이 코딩테스트 대비 강의](https://www.inflearn.com/course/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8/dashboard)
