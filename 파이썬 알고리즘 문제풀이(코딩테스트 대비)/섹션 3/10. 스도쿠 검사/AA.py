import os
import sys
#sys.stdin = open(os.path.join(sys.path[0], "in1.txt"), 'rt')

n = 9
a = [list(map(int, input().split())) for _ in range(n)]



def check_row():
    for i in range(n):
        c = [False] * 10
        for j in range(n):
            c[a[i][j]] = True
        
        if a.count(True) == 9:
            return False

    return True

def check_col():
    for i in range(n):
        c = [False] * 10
        for j in range(n):
            c[a[i][j]] = True
        
        if a.count(True) != 9:
            return False

    return True

def check_box(s):
    for i in range(s, s + 3):
        c = [False] * 10
        for j in range(s, s + 3):
            c[a[i][j]] = True

    if a.count(True) != 9:
        return False
    
    return True

def check():
    c = [False] * 9

    for i in range(0, n, 3):
        for j in range(0, n, 3):
            c[i + (j // 3)] = check_box(i)
    
    if a.count(True) != 9:
        return False
    else:
        return True

answer = True
answer = check_row()
answer = check_col()
answer = check()

print('YES' if answer else 'NO')
