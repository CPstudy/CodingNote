import os
import sys
sys.stdin = open(os.path.join(sys.path[0], "in1.txt"), 'rt')

n = int(input())
ch = [False] * (n + 1)

def dfs(v):
    if v == n + 1:
        for i in range(1, n + 1):
            if ch[i] == True:
                print(i, end=' ')
        print()
    else:
        ch[v] = True
        dfs(v + 1)
        ch[v] = False
        dfs(v + 1)

dfs(1)