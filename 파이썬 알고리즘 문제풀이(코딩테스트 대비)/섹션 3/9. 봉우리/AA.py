import os
import sys
#sys.stdin = open(os.path.join(sys.path[0], "in1.txt"), 'rt')

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

answer = 0

for i in range(n):
    for j in range(n):
        top = 0
        left = 0
        right = 0
        bottom = 0

        if i > 0:
            top = a[i - 1][j]
        
        if i < n - 1:
            bottom = a[i + 1][j]
        
        if j > 0:
            left = a[i][j - 1]

        if j < n - 1:
            right = a[i][j + 1]
        
        if a[i][j] > max(top, left, right, bottom):
            answer += 1

print(answer)