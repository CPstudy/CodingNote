import os
import sys
import itertools as it
sys.stdin = open(os.path.join(sys.path[0], "in1.txt"), 'rt')

n, f = map(int, input().split())
res = [0] * n
b = [1] * n
ch = [False] * (n + 1)

for i in range(1, n):
    b[i] = b[i - 1] * (n - i) // i


def dfs(idx, summation):
    if idx == n and summation == f:
        for x in res:
            print(x, end=' ')
        print()
    else:
        for i in range(1, n + 1):
            if ch[i] == False:
                res[idx] = i
                ch[i] = True
                dfs(idx + 1, summation + res[idx] * b[idx])
                ch[i] = False

dfs(0, 0)
