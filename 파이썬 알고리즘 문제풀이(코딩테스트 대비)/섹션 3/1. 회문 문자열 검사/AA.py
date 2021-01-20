import os
import sys
#sys.stdin = open(os.path.join(sys.path[0], "in1.txt"), 'rt')

n = int(input())

for i in range(n):
    word = input()
    word = word.lower()
    reverse = word[::-1]

    if word == reverse:
        print('#%d YES' %(i + 1))
    else:
        print('#%d NO' %(i + 1))