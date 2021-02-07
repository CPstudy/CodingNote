import os
import sys
#sys.stdin = open(os.path.join(sys.path[0], "in5.txt"), 'rt')

n, k = map(int, input().split())
a = list(map(int, input().split()))
m = int(input())
a.sort()

res = [0] * k
answer = 0

def dfs(index, s, summation):
    if index == k:
        if summation % m == 0:
            global answer
            answer += 1
    else:
        for i in range(s, n):
            res[index] = a[i]
            dfs(index + 1, i + 1, summation + a[i])

dfs(0, 0, 0)
print(answer)