import os
import sys
#sys.stdin = open(os.path.join(sys.path[0], "in1.txt"), 'rt')

n = int(input())
a = []

for _ in range(n):
    a.append(list(map(int, input().split())))

a.sort(key=lambda x: (x[1], x[0]))

end = a[0][1]
answer = 1

for i in range(1, n):
    if a[i][0] >= end:
        answer += 1
        end = a[i][1]

print(answer)