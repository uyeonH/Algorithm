
'''
# 가장 큰 수

숫자 하나가 주어지면, 해당 숫자의 자리수들 중 m개의 숫자를 제거하여 가장 큰 수를 만들어야한다. 
단, 숫자의 순서는 유지해야한다.

예를 들어, 5276832가 주어지고 3개의 자릿수를 제거한다면 7823이 가장 큰 수가 된다.

# input
9977252641 5

# output
99776

'''

import sys
sys.stdin = open("in1.txt", "r")

num,m =map(int, input().split())
num=list(map(int,str(num)))

stack=[]

for x in num:
   # 스택이 비어있지 않고, 지워야할 숫자가 남아있으며, 스택의 마지막 숫자가 지금 넣을 숫자보다 작다면 제거하기
    while stack and m>0 and stack[-1]<x:
        stack.pop()
        m-=1
    # 빼는 작업이 완료되었고 x보다 큰 숫자만 남아있으면 x 넣기
    stack.append(x)

# 더 지워야할 숫자가 남아있다면 뒤에 m개 제거하기
if m!=0:
    stack=stack[:-m]
    
print("".join(list(map(str,stack))))
