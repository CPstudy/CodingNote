import os
import sys
#sys.stdin = open(os.path.join(sys.path[0], "in5.txt"), 'rt')

c, n = map(int, input().split())
a = [int(input()) for _ in range(n)]
a.sort(reverse=True)
total = sum(a)
answer = 0

def dfs(index, weight, tsum):
    global answer
    if weight + (total - tsum) < answer:
        return

    if weight > c:
        return

    if index == n:
        if weight <= c:
            answer = max(answer, weight)

    else:
        dfs(index + 1, weight + a[index], tsum + a[index])
        dfs(index + 1, weight, tsum + a[index])

dfs(0, 0, 0)
print(answer)