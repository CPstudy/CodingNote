import os
import sys
#sys.stdin = open(os.path.join(sys.path[0], "in1.txt"), 'rt')

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

res = list()
s = 0

for i in range(n):
    for j in range(n):
        s += a[i][j]
    res.append(s)
    s = 0

for i in range(n):
    for j in range(n):
        s += a[j][i]
    res.append(s)
    s = 0

for i in range(n):
    s += a[i][i]

res.append(s)
s = 0

for i in range(n):
    s += a[i][n - 1 - i]

res.append(s)
s = 0

print(max(res))