
'''

# 후위식이 주어졌을 때 연산하기

'''

import sys
sys.stdin = open("input.txt", "r")
a = input()
stack = []
for x in a:
    if x.isdecimal():
        stack.append(int(x))
    else:
        if x == '+':
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(b + a)
        elif x == '-':
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(b - a)
        elif x == '*':
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(b * a)
        elif x == '/':
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(b / a)

print(stack[0])
