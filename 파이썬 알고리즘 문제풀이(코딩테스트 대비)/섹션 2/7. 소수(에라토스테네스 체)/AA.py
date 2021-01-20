import os
import sys
#sys.stdin = open(os.path.join(sys.path[0], "in1.txt"), 'rt')

n = int(input())
ch = [False] * (n + 1)
cnt = 0
for i in range(2, n + 1):
    if ch[i] == False:
        cnt += 1
        for j in range(i, n + 1, i):
            ch[j] = True

print(cnt)