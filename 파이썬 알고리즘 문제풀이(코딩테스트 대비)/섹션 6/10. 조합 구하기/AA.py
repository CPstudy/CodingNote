import os
import sys
sys.stdin = open(os.path.join(sys.path[0], "in1.txt"), 'rt')

n, m = map(int, input().split())
res = [0] * m
answer = 0

def dfs(L, s):
    if L == m:
        for x in res:
            print(x, end=' ')
        global answer
        answer += 1
        print()
    else:
        for i in range(s, n + 1):
            res[L] = i
            dfs(L + 1, i + 1)

dfs(0, 1)
print(answer)