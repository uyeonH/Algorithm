'''
# 후위표기식 만들기 (Stack)

'''

import sys

sys.stdin = open("in2.txt", "r")
a = input()  # (3+5)*2
op = ['+', '-', '*', '/', '(', ')']
stack = []
res = ''  # 35+2*
for x in a:
    if x.isdecimal():
        res += x
    else:
        if x == '(':  # 여는 괄호일 때,
            stack.append(x)  # 스택에 넣기
        elif x == '*' or '/':  # 곱하기나 나누기일 때,
            # 스택 젤위에 *나 /가 있으면 res에 계속 이어쓰기
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()
            # 마지막으로 현재 * 또는 /를 이어붙임
            stack.append(x)

        elif x == '+' or '-':  # + 또는 -일 경우
            # 스택이 비어있지 않고 마지막이 (가 아니면
            # (를 만나기 전까지 괄호 안의 부호라는 의미이므로
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(x)

        elif x == ')': # 닫는 괄호이면
            while stack and stack[-1] != '(': # 여는 괄호 나올 때까지 꺼내기
                res += stack.pop()
            stack.pop()

while stack:
    res += stack.pop()
    
print(res)
