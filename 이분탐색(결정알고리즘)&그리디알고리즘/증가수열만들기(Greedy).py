'''
# 증가수열 만들기

1부터 N까지 모든 자연수로 구성된 길이 N의 수열이 주어진다.
이 수열의 왼쪽 끝 또는 오른쪽 끝 숫자 중 하나를 가져와 나열하여 가장 긴 증가수열을 만든다.

첫째 줄에 자연수 N
둘째 줄에 N개로 구성된 수들이 주어진다.

출력은 첫째 줄에 최대 증가수열의 길이를 출력하고, 
둘째 줄에 순서대로 왼쪽 끝에서 가져갔으면 'L', 오른쪽 끝에서 가져갔으면 'R'을 써간 문자열을 출력한다.

# input
5
2 4 5 1 3

#output
4
LRLL

# 풀이
  처음에는 이중 if문을 두개써서 크기 비교를 해야하나 했는데,
  tmp라는 리스트를 임시로 하나 만들어서 양쪽에서 하나씩 꺼내어 비교하면 된다. 
  굿아이디어!
 
'''

import sys

sys.stdin = open("in1.txt", "r")
n = int(input())
number = list(map(int, input().split()))
ep = 0 # 증가수열의 마지막 값
lt = 0
rt = n - 1
tmp = []
res=""
while lt <= rt:

    if number[lt] >= ep: # 왼쪽 끝 값과 증가수열의 마지막 값 비교
        tmp.append((number[lt], 'L')) # 튜플 형태로 L 값도 같이 저장

    if number[rt] >= ep: # 오른쪽 끝 값과 증가수열의 마지막 값 비교
        tmp.append((number[rt], 'R'))

    tmp.sort() # 값으로 정렬 (오름차순

    if len(tmp) == 0: #tmp가 비었을 경우
        break
    else:
        res = res + tmp[0][1] # tmp에 있는 수 중 더 작은 수의 L, R
        ep=tmp[0][0] 

        if tmp[0][1]=='L': # 왼쪽 값이 더 작을 경우 왼쪽 포인터를 늘림
            lt+=1
        else:
            rt-=1

    tmp.clear()

print(len(res))
print(res)
