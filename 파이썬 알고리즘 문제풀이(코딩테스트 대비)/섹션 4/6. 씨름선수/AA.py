import os
import sys
#sys.stdin = open(os.path.join(sys.path[0], "in1.txt"), 'rt')

n = int(input())
a = []
fail = 0

for _ in range(n):
    a.append(tuple(map(int, input().split())))

a.sort(reverse=True)

largest = 0
answer = 0

for h, w in a:
    if w > largest:
        largest = w
        answer += 1

print(answer)