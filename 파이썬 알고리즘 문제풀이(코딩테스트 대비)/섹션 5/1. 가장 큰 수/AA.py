import os
import sys
#sys.stdin = open(os.path.join(sys.path[0], "in2.txt"), 'rt')

n, m = map(int, input().split())
a = list(map(int, str(n)))
stack = []

for x in a:
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1
    
    stack.append(x)
            
if m != 0:
    stack = stack[:-m]

print(''.join(map(str, stack)))