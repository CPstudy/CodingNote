import os
import sys
#sys.stdin = open(os.path.join(sys.path[0], "in1.txt"), 'rt')

n = 7
m = 5
a = [list(map(int, input().split())) for _ in range(n)]

answer = 0

# 가로 회문 검사
for i in range(n):
    for j in range(n - m + 1):
        if a[i][j] == a[i][j + 4] and a[i][j + 1] == a[i][j + 3]:
            answer += 1
        

# 세로 회문 검사
for i in range(n - m + 1):
    for j in range(n):
        if a[i][j] == a[i + 4][j] and a[i + 1][j] == a[i + 3][j]:
            answer += 1

print(answer)