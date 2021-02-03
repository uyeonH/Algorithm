# https://www.acmicpc.net/problem/1260
# 백준 1260번

import pprint

def dfs(V):
    visited_list[V]=1
    print(V,end=' ')
    for i in range(1,N+1):
        if visited_list[i]==0 and matrix[V][i]==1:
            dfs(i)


def bfs(V):
    queue=[V]
    visited_list[V]=0
    while queue:
        V=queue.pop(0)
        print(V, end=' ')
        for i in range(1,N+1):
            # 방문하지 않았고, 현재 위치에서 연결된 통로가 있으면
            if visited_list[i]==1 and matrix[V][i]==1:
                queue.append(i)
                visited_list[i]=0




if __name__=="__main__":
    N, M, V = map(int, input().split())
    #N,M,V=4,5,1
    matrix = [[0] *(N+1) for i in range(N+1)]
    visited_list=[0]*(N+1)
    for i in range(M):
        a,b=map(int,input().split())
        matrix[a][b]=matrix[b][a]=1

    #pprint.pprint(matrix)
    dfs(V)
    print()
    bfs(V)
    
