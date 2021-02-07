import os
import sys
#sys.stdin = open(os.path.join(sys.path[0], "in1.txt"), 'rt')

k, n = map(int, input().split())
a = []
for _ in range(k):
    a.append(int(input()))

res = 0

def search(start, end, res):
    if start >= end:
        return start
        
    mid = (start + end) // 2
    cnt = 0

    for x in a:
        cnt += x // mid
    
    if cnt >= n:
        return search(mid + 1, end, mid)
    else:
        return search(start, mid - 1, res)

print(search(0, max(a), 0))