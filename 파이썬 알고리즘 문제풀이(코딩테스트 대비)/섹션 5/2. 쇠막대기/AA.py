import os
import sys
#sys.stdin = open(os.path.join(sys.path[0], "in1.txt"), 'rt')

a = list(map(str, input()))
stack = []
wood = 0

for i in range(0, len(a) - 1):
    if a[i] == '(' and a[i + 1] == ')':
        # 레이저
        wood += len(stack)
    elif a[i] == '(' and a[i + 1] == '(':
        wood = wood + 1
        stack.append('(')
    elif a[i] == ')' and a[i + 1] == ')' and stack:
        stack.pop()
    else:
        pass

print(wood)