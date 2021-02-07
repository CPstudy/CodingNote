import os
import sys
#sys.stdin = open(os.path.join(sys.path[0], "in1.txt"), 'rt')

n, m = map(int, input().split())
res = [0] * m
ch = [False] * (n + 1)
count = 0

def dfs(idx):
    global count
    if idx == m:
        for x in res:
            print(x, end=' ')
        print()
        count += 1
    else:
        for i in range(1, n + 1):
            if ch[i] == False:
                res[idx] = i
                ch[i] = True

                dfs(idx + 1)
                ch[i] = False

dfs(0)
print(count)