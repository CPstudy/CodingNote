import os
import sys
#sys.stdin = open(os.path.join(sys.path[0], "in1.txt"), 'rt')

n, m = map(int, input().split())
count = 0
res = [0] * m
count = 0

def comb(idx):
    global count
    if idx == m:
        for x in range(m):
            print(res[x], end=' ')
        print()
        count += 1
        return
    else:
        for i in range(1, n + 1):
            res[idx] = i
            comb(idx + 1)

comb(0)
print(count)