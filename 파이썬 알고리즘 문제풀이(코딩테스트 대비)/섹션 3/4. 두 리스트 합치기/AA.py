import os
import sys
# sys.stdin = open(os.path.join(sys.path[0], "in1.txt"), 'rt')

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
c = list()

p1, p2 = 0, 0

while p1 < n and p2 < m:
    x = a[p1]
    y = b[p2]

    if x < y:
        c.append(x)
        p1 += 1
    else:
        c.append(y)
        p2 += 1

if p1 < n:
    c = c + a[p1:]

if p2 < m:
    c = c + b[p2:]

for x in c:
    print(x, end=' ')