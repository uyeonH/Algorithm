import itertools as it
import sys

sys.stdin = open("in1.txt", "rt")

if __name__ == "__main__":
    n, f = map(int, input().split())
    b = [1] * n
    a = list(range(1, n + 1))

    for i in range(1, n):
        b[i] = b[i - 1] * (n - i) // i

    for tmp in it.permutations(a):
        sum_ = 0
        for L, x in enumerate(tmp):
            sum_ += x * b[L]
        #print(sum_)
        if sum_ == f:
            for x in tmp:
                print(x, end=' ')
            break
