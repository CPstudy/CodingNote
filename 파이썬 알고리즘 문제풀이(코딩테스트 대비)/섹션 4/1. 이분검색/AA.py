import os
import sys
#sys.stdin = open(os.path.join(sys.path[0], "in1.txt"), 'rt')

n, m = map(int, input().split())
a = list(map(int, input().split()))

def binary_search(left, right, find):
    mid = (left + right) // 2

    if a[mid] == find:
        return mid + 1
    elif find < a[mid]:
        return binary_search(left, mid - 1, find)
    else:
        return binary_search(mid + 1, right, find)

a.sort()
print(binary_search(0, len(a) - 1, m))