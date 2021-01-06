'''
#input
3

#output
1 2 3 
1 2 
1 3 
1 
2 3 
2 
3 


'''

import sys
sys.stdin=open("in1.txt", "r")
def DFS(v):
    if v == n + 1:
        for i in range(1, n + 1):
            if ch[i] == 1:
                print(i, end=' ')
        print()
    else:
        ch[v] = 1
        DFS(v + 1)
        ch[v] = 0
        DFS(v + 1)


if __name__ == "__main__":
    n = int(input())
    ch = [0] * (n + 1)  # 체크변수
    DFS(1)
