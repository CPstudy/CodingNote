import os
import sys
#sys.stdin = open(os.path.join(sys.path[0], "in1.txt"), 'rt')

n = int(input())
a = list(map(int, input().split()))

answer = ''
low = 0

for _ in range(n):
    if len(a) == 1 and a[-1] > low:
        answer += 'L'
        break

    left = a[0] if a[0] > low else 500
    right = a[-1] if a[-1] > low else 500

    if left - low < right - low:
        a.pop(0)
        answer += 'L'
        low = left
    elif left - low > right - low:
        a.pop(-1)
        answer += 'R'
        low = right

print(len(answer))
print(answer)