import os
import sys
sys.stdin = open(os.path.join(sys.path[0], "in1.txt"), 'rt')

n, m = map(int, input().split())
a = list(map(int, input().split()))

def dvd(capacity):
    cnt = 1
    result = 0

    for x in a:
        if result + x > capacity:
            cnt += 1
            result = x
        else:
            result += x
    
    return cnt

def search(start, end, res):
    if start == res or end == res:
        return res

    mid = (start + end) // 2
    
    count = dvd(mid)

    if mid >= max(a) and count <= m:
        return search(start, mid - 1, mid)
    else:
        return search(mid + 1, end, res)

print(search(min(a), sum(a), 0))