def DFS(L):
    global result
    if L == r:
        print(result)

        return
    for i in range(len(n)):
        if checkList[i] == 0:
            checkList[i] = 1
            result[L]=n[i]
            DFS_permu(L + 1)
            checkList[i] = 0


n = [1, 2, 3]
r = 3
checkList = [0] * len(n)
result = [0]*r
DFS(0)
