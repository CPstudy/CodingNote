import os
import sys
#sys.stdin = open(os.path.join(sys.path[0], "in1.txt"), 'rt')

n, c = map(int, input().split())
Line = []

for _ in range(n):
    Line.append(int(input()))

Line.sort()
lt = 1
rt = Line[-1]

def count_horse(d):
    cnt = 1
    ep = Line[0]

    for i in range(1, n):
        if Line[i] - ep >= d:
            cnt += 1
            ep = Line[i]
    
    return cnt

while lt <= rt:
    mid = (lt + rt) // 2

    if count_horse(mid) >= c:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)