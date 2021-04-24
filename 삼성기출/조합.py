def DFS(L, begain):
    if L==r:
        print(result)
        return
    for i in range(begain,len(li)):
        result[L]=[i]
        DFS(L+1,i+1)
li=[1,2,3,4]
r=3
result=[0]*r
DFS(0,0)


