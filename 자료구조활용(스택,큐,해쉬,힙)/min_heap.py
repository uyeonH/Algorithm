

import sys
import heapq as hq

sys.stdin = open("in1.txt", "r")
a = []
while True:
    print(a)
    n = int(input())

    if n == -1:
        break

    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(hq.heappop(a))
    else:
        hq.heappush(a, n)
