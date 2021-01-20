import os
import sys
sys.stdin = open(os.path.join(sys.path[0], "in1.txt"), 'rt')

n, m = map(int, input().split())
cnt = [0] * (n + m + 1)
max = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        cnt[i + j] += 1

for i in range(n + m + 1):
    if cnt[i] > max:
        max = cnt[i]

for i in range(n + m + 1):
    if cnt[i] == max:
        print(i, end=' ')