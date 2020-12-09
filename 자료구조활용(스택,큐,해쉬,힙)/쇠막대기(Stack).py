
import sys

sys.stdin = open("in3.txt", "r")

data = input()

stack = []

cnt = 0

for i in range(len(data)):

    if data[i] == '(':
        stack.append(data[i])
        
    else:
        stack.pop()

        if data[i - 1] == '(':
            cnt += len(stack)
            
        else:
            cnt += 1

print(cnt)

