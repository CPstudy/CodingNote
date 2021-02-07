import os
import sys
#sys.stdin = open(os.path.join(sys.path[0], "in1.txt"), 'rt')

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
b = [list(map(int, input().split())) for _ in range(m)]

def move(array, direction, count):
    tmp = [0] * n

    for idx, x in enumerate(array):
        if direction == 0:  # 왼쪽
            if idx < count:
                tmp[n - count + idx] = x
            else:
                tmp[idx - count] = x
        else:
            if idx >= n - count:
                tmp[idx - (n - count)] = x
            else:
                tmp[idx + count] = x
    
    return tmp

def print_board():
    answer = 0
    cnt = 0
    for i in range(n):
        for j in range(n):
            if cnt <= j < n - cnt:
                answer += a[i][j]
    
        if i >= n // 2:
            cnt -= 1
        else:
            cnt += 1
    
    print(answer)

for x in b:
    a[x[0] - 1] = move(a[x[0] - 1], x[1], x[2])

print_board()

