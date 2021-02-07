import os
import sys
sys.stdin = open(os.path.join(sys.path[0], "in4.txt"), 'rt')

n = int(input())
a = list(map(int, input().split()))
summation = sum(a)
answer = 0

def dfs(index, s):
    if s > summation // 2:
        return
        
    if index == n:
        if summation - s == s:
            global answer
            answer = 1

    else:
        dfs(index + 1, s + a[index])
        dfs(index + 1, s)

dfs(0, 0)
if answer > 0:
    print('YES')
else:
    print('NO')