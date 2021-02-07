import os
import sys
from collections import deque
#sys.stdin = open(os.path.join(sys.path[0], "in2.txt"), 'rt')

s = input()
n = int(input())
e = [list(input()) for _ in range(n)]

for idx, word in enumerate(e):
    a = deque(list(s))
    for x in word:
        if a:
            c = a[0]
            if any(x == aa for aa in a):
                if x == c:
                    a.popleft()
                else:
                    print('#%d NO' %(idx + 1))
                    break
    
    else:
        if a:
            print('#%d NO' %(idx + 1))
        else:
            print('#%d YES' %(idx + 1))