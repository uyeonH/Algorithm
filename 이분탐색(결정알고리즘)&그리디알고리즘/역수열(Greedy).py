
'''
# 역수열

1부터 n까지의 수를 한 번씩만 사용하여 이루어진 수열이 있을 때, 1부터 n까지 각각의 수 앞에 놓여있는 자신보다 큰 수들의 개수를 
수열로 표현한 것을 역수열이라고 한다.

예를 들어, 

4 8 6 2 5 1 3 7 수열이 있으면 

1앞에 놓인 1보다 큰 수는 5개이고, 2앞에 놓인 2보다 큰 수는 3개이고... 이렇다

따라서 위 수열의 역수열은 5 3 4 0 2 1 1 0 이 된다. 

역수열이 주어졌을 때, 원래의 수열을 구하는 프로그램을 작성해라.

# input
8 
5 3 4 0 2 1 1 0

# output
4 8 6 2 5 1 3 7

'''

import sys

sys.stdin = open("in1.txt", "r")
n = int(input())
number = list(map(int, input().split()))

res=[]
for i in range(n):
    res.insert(number[n-1-i],n-i)
res=list(map(str,res))
print(" ".join(res))

