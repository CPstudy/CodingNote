import os
import sys
#sys.stdin = open(os.path.join(sys.path[0], "in1.txt"), 'rt')

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
t = n // 2 + 1
cnt = 0

for i in range(n):
    for j in range(n):
        s = abs(n - i - t)
        e = n - 1 - s

        if s <= j <= e:
            cnt += a[i][j]

print(cnt)