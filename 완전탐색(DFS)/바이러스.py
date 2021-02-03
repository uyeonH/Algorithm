# 백준 2606번
# https://www.acmicpc.net/problem/2606
import pprint
def bfs(V):
    global res
    queue = [V]
    visited_list[V] = 1
    while queue:
        from_ = queue.pop(0)
        #print(from_, end=' ')
        for to_ in range(1, N + 1):
            if visited_list[to_] == 0 and matrix[from_][to_] == 1:
                queue.append(to_)
                visited_list[to_] = 1

def dfs(V):
    visited_list[V] = 1
    for i in range(1, N + 1):
        if visited_list[i] == 0 and matrix[V][i] == 1:
            dfs(i)


if __name__ == "__main__":
    N = int(input())
    M = int(input())
    res = 0
    matrix = [[0] * (N + 1) for _ in range(N + 1)]
    visited_list = [0] * (N + 1)
    for i in range(M):
        a, b = map(int, input().split())
        matrix[a][b] =matrix[b][a]= 1
    #dfs(1)
    bfs(1)
    for i in visited_list:
        if i:
            res+=1

    print(res-1)

'''
7
6
1 2
2 3
1 5
5 2
5 6
4 7
'''
