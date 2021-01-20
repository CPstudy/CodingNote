import os
import sys
#sys.stdin = open(os.path.join(sys.path[0], "in1.txt"), 'rt')

n = int(input())
scores = list(map(int, input().split()))

res = 0
score = 0

for s in scores:
    if s == 1:
        res += 1
        score += res
    else:
        res = 0

print(score)