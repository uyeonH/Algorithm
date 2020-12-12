# dictionary 활용
#사용하지 않은 단어 찾기
# dictionary를 활용하여 예쁘게 푼다.

import sys

#sys.stdin = open("in1.txt", "r")
n = int(input())
p=dict()

for i in range(n):
    word=input()
    p[word]=1
#print(p)

for i in range(n-1):
    word=input()
    p[word]=0
#print(p)

for key,value in p.items():
    if value==1:
        print(key)
        break
 
