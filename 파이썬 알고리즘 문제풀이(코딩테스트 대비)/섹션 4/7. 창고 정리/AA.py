import os
import sys
#sys.stdin = open(os.path.join(sys.path[0], "in1.txt"), 'rt')

# 창고 가로 길이
L = int(input())

# 높이
a = list(map(int, input().split()))

# 높이 조정 횟수
M = int(input())

for _ in range(M):
    a.sort()
    a[0] += 1
    a[-1] -= 1


a.sort()

print(a[-1] - a[0])